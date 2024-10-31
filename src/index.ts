import { Hono } from 'hono'
import { prettyJSON } from 'hono/pretty-json'

import { cors } from 'hono/cors'
import { csrf } from 'hono/csrf'
import { bearerAuth } from 'hono/bearer-auth'
import { sign, verify } from 'hono/jwt'

import api from './v2'

// Only host that is allowed access to this API
const ALLOWED_HOST = 'kylechapman.dev'

type Bindings = {
  USERNAME: string
  PASSWORD: string
  JWT_SECRET: string
}

const app = new Hono<{ Bindings: Bindings }>()
app.notFound((c) => c.json({ message: 'Not Found', ok: false }, 404))

// -- Middleware --
app.use(prettyJSON())

// Only allow requests from my domain
app.use('/*', cors({
  origin: (origin, c) => {
    return origin.endsWith(ALLOWED_HOST)
      ? origin
      : `https://${ALLOWED_HOST}`
  },
  allowMethods: ['GET', 'POST']
}))

// CSRF protection
app.use(csrf({ origin: ALLOWED_HOST }))

// -- Routes --
app.get('/', (c) => c.json({ message: 'Welcome!', ok: true }, 200))

app.post('/authorize', async (c) => {
  const VALID_USERNAME = c.env.USERNAME
  const VALID_PASSWORD = c.env.PASSWORD

  const { username, password } = await c.req.json()
  if (username !== VALID_USERNAME || password !== VALID_PASSWORD) {
    return c.json({ message: 'Unauthorized', ok: false }, 401)
  }

  const now = Math.floor(Date.now() / 1000)
  const payload = {
    role: 'admin',
    exp: now + 30, // Token expires in 30 seconds
    iat: now
  }

  const token = await sign(payload, c.env.JWT_SECRET)
  return c.json({
    payload,
    token
  })
})

// Route with new API
app.use('/v2/*', bearerAuth({
  verifyToken: async (token, c) => {
    try {
      await verify(token, c.env.JWT_SECRET)
    } catch (e) {
      return false
    }

    return true
  }
}))
app.route('/v2', api)

export default app
