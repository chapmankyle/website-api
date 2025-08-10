import { Hono } from 'hono'
import { prettyJSON } from 'hono/pretty-json'

import { cors } from 'hono/cors'
import { csrf } from 'hono/csrf'
import { bearerAuth } from 'hono/bearer-auth'
import { sign, verify } from 'hono/jwt'

import api from './v2'

// Only host that is allowed access to this API
const ALLOWED_HOST = 'kylechapman.dev'

// URLs that are allowed to access this API
const ALLOWED_URLS = [`https://${ALLOWED_HOST}`]

// Token expiration times (in seconds)
const TOKEN_EXPIRY = {
  development: 3600, // 1 hour in development
  production: 30     // 30 seconds in production
}

// Refresh token expiry times (in seconds)
const REFRESH_TOKEN_EXPIRY = {
  development: 86400, // 24 hours in development
  production: 3600    // 1 hour in production
}

export type Bindings = {
  USERNAME: string
  PASSWORD: string
  JWT_SECRET: string
  ENVIRONMENT?: string // Optional environment variable
}

const app = new Hono<{ Bindings: Bindings }>()
app.notFound((c) => c.json({ message: 'Not Found', ok: false }, 404))

// -- Middleware --
app.use(prettyJSON())

// Only allow requests from certain URLs
app.use('/*', cors({
  origin: (origin, c) => {
    const isDevelopment = c.env.ENVIRONMENT === 'development'
    return isDevelopment
      ? origin
      : ALLOWED_URLS.includes(origin) ? origin : `https://${ALLOWED_HOST}`
  },
  allowMethods: ['GET', 'POST'],
  allowHeaders: ['Authorization', 'Content-Type'],
  exposeHeaders: ['Content-Length'],
  maxAge: 3600
}))

// CSRF protection
app.use(csrf({ origin: ALLOWED_HOST }))

// -- Routes --
app.get('/', (c) => c.json({ message: 'Welcome!', ok: true }, 200))

app.post('/authorize', async (c) => {
  const VALID_USERNAME = c.env.USERNAME
  const VALID_PASSWORD = c.env.PASSWORD

  // Determine environment (default to production for security)
  const environment = c.env.ENVIRONMENT === 'development' ? 'development' : 'production'
  console.log(`Running in ${environment} environment`)

  const { username, password } = await c.req.json()
  if (username !== VALID_USERNAME || password !== VALID_PASSWORD) {
    return c.json({ message: 'Unauthorized', ok: false }, 401)
  }

  const now = Math.floor(Date.now() / 1000)
  const payload = {
    role: 'admin',
    exp: now + TOKEN_EXPIRY[environment], // Token expiry based on environment
    iat: now
  }

  // Create refresh token with longer expiration
  const refreshPayload = {
    role: 'refresh',
    exp: now + REFRESH_TOKEN_EXPIRY[environment], // Refresh token expiry based on environment
    iat: now
  }

  const token = await sign(payload, c.env.JWT_SECRET)
  const refreshToken = await sign(refreshPayload, c.env.JWT_SECRET)

  return c.json({
    payload,
    token,
    refreshToken
  })
})

// Route with new API
app.use('/v2/*', bearerAuth({
  verifyToken: async (token, c) => {
    try {
      const payload = await verify(token, c.env.JWT_SECRET)

      // Check if token is expired by checking current time against exp
      const now = Math.floor(Date.now() / 1000)
      if (payload.exp && payload.exp < now) {
        console.error('Token expired')
        return false
      }

      // Check if token has the correct role
      if (payload.role !== 'admin') {
        console.error('Invalid role in token')
        return false
      }

      return true
    } catch (e) {
      console.error('Token verification failed:', e)
      return false
    }
  }
}))
app.route('/v2', api)

export default app
