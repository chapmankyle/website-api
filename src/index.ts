import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { prettyJSON } from 'hono/pretty-json'

import api from './v2'

// Create app
const app = new Hono()
app.get('/', (c) => c.text('Welcome!'))
app.notFound((c) => c.json({ message: 'Not Found', ok: false }, 404))

// Middleware
app.use(prettyJSON())
app.use('/*', cors({
  origin: (origin, c) => {
    return origin.endsWith('kylechapman.dev')
      ? origin
      : 'https://kylechapman.dev/'
  },
  allowMethods: ['GET']
}))

// Route with new API
app.route('/v2', api)

export default app
