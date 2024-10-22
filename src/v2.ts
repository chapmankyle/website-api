import { Hono } from 'hono'
import { cors } from 'hono/cors'

import { default as data } from './data.json'

interface Experience {
  id: number
  startDate: string
  endDate: string
  title: string
  type: string
  company: string
  description: string
  technologies: string[]
  dateAsString?: string
}

/** Base URL for the API */
const BASE_URL = '/v2'

/** Parses the data from the JSON file, adding any necessary information */
const parseData = () => {
  const parsed = JSON.parse(JSON.stringify(data))
  const hasExperience = parsed.experience != null && Array.isArray(parsed.experience) && parsed.experience.length > 0

  // Ensure experience is sorted by id
  if (hasExperience) {
    parsed.experience.sort((a: Experience, b: Experience) => b.id - a.id)

    const mostRecent = parsed.experience[0]
    if (mostRecent.endDate.toLowerCase() === 'present' && typeof mostRecent.dateAsString === 'string') {
      const now = new Date()
      const started = new Date(mostRecent.dateAsString)

      let months = (now.getFullYear() - started.getFullYear()) * 12
      months -= started.getMonth()
      months += now.getMonth() + 1

      let years = Math.floor(months / 12)
      months = months % 12

      const yearsStr = years > 0 ? `${years} yr${years === 1 ? '' : 's'}` : ''
      const monthStr = months > 0 ? `${months} mo${months === 1 ? '' : 's'}` : ''

      parsed.experience[0].duration = yearsStr.length > 0 ? `${yearsStr} ${monthStr}` : monthStr
    }
  }

  return parsed
}

// Make sure data is parsed before we start
const PARSED_DATA = parseData()

// Create API routes
const api = new Hono()
api.use(`${BASE_URL}/*`, cors())

// Gets all data or subset from our data file
api.get(`${BASE_URL}/:id`, c => {
  const id = c.req.param('id')
  if (!id) {
    return c.json({ message: 'Not Found', ok: false }, 404)
  }

  if (id === 'all') {
    return c.json({ data: PARSED_DATA, ok: true }, 200)
  }

  const item = PARSED_DATA[id]
  if (!item) {
    return c.json({ message: 'Not Found', ok: false }, 404)
  }

  return c.json({ data: item, ok: true }, 200)
})

export default api
