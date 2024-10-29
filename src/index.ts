import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { csrf } from 'hono/csrf'
import { prettyJSON } from 'hono/pretty-json'

import api from './v2'

// Only host that is allowed access to this API
const ALLOWED_HOST = 'kylechapman.dev'

// Create app
const app = new Hono()
app.get('/', (c) => c.text('Welcome!'))
app.notFound((c) => c.json({ message: 'Not Found', ok: false }, 404))

app.use(prettyJSON())

// Only allow requests from my domain
app.use('/*', cors({
  origin: (origin, c) => {
    return origin.endsWith(ALLOWED_HOST)
      ? origin
      : `https://${ALLOWED_HOST}`
  },
  allowMethods: ['GET']
}))

// CSRF protection
app.use(csrf({ origin: ALLOWED_HOST }))

// Route with new API
app.route('/v2', api)

export default app
