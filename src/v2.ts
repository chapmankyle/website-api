import { Hono } from 'hono'
import { cors } from 'hono/cors'

import { default as data } from './data.json'

import type { IData } from './types'

/** Base URL for the API */
const BASE_URL = '/v2'

/** Parses the data from the JSON file */
const parseData = (): IData => {
  const parsed = (JSON.parse(JSON.stringify(data))) as IData

  // Ensure experience is sorted by id
  if (parsed.experience != null && Array.isArray(parsed.experience) && parsed.experience.length > 0) {
    parsed.experience.sort((a, b) => b.id - a.id)
  }

  return parsed
}

/**
 * Adds the duration to the experience object at the given index.
 * @param index Index into the experience array to add duration to.
 * @param data Data object to modify.
 */
const addDuration = (index: number, data: IData): void => {
  const experience = data.experience
  if (!experience || !Array.isArray(experience) || experience.length < 1) {
    return
  }

  const mostRecent = experience[index]
  if (typeof mostRecent.dateAsString !== 'string') {
    return
  }

  const now = new Date() // Since we are inside a worker, we cannot use the date from the global context
  const started = new Date(mostRecent.dateAsString)

  let months = (now.getFullYear() - started.getFullYear()) * 12
  months -= started.getMonth()
  months += now.getMonth() + 1

  const years = Math.floor(months / 12)
  months = months % 12

  const yearsStr = years > 0 ? `${years} yr${years === 1 ? '' : 's'}` : ''
  const monthStr = months > 0 ? `${months} mo${months === 1 ? '' : 's'}` : ''

  data.experience[index].duration = yearsStr.length > 0 ? `${yearsStr} ${monthStr}` : monthStr
}

// Make sure we have a parsed version of the data
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
    if (typeof PARSED_DATA.experience[0].duration != 'string' || PARSED_DATA.experience[0].duration.length < 1) {
      addDuration(0, PARSED_DATA)
    }

    return c.json({ data: PARSED_DATA, ok: true }, 200)
  }

  let item = PARSED_DATA[id]
  if (!item) {
    return c.json({ message: 'Not Found', ok: false }, 404)
  }

  if (id === 'experience' && (typeof item[0].duration != 'string' || item[0].duration.length < 1)) {
    addDuration(0, PARSED_DATA)
    item = PARSED_DATA[id]
  }

  return c.json({ data: item, ok: true }, 200)
})

export default api
