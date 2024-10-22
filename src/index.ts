import { Hono } from 'hono'
import { prettyJSON } from 'hono/pretty-json'

import api from './v2'

// Create app
const app = new Hono()
app.get('/', (c) => c.text('Welcome!'))
app.use(prettyJSON())
app.notFound((c) => c.json({ message: 'Not Found', ok: false }, 404))


// Route with new API
app.route('/api', api)

export default app
