import { Hono } from 'hono'
import { cors } from 'hono/cors'

import { default as data } from './data.json'

/** Base URL for the API */
const BASE_URL = '/v2'

// Create API routes
const api = new Hono()
api.use(`${BASE_URL}/*`, cors())

// Gets all data or subset from our data file
api.get(`${BASE_URL}/:id`, c => {
  const id = c.req.param('id')
  if (!id) {
    return c.json({ message: 'Not Found', ok: false }, 404)
  }

  const allData = JSON.parse(JSON.stringify(data))

  if (id === 'all') {
    return c.json({ data: allData, ok: true }, 200)
  }

  const item = allData[id]
  if (!item) {
    return c.json({ message: 'Not Found', ok: false }, 404)
  }

  return c.json({ data: item, ok: true }, 200)
})

export default api
