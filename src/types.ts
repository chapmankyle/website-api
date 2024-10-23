export interface IMetadata {
  name: string
  initials: string
  url: string
  location: string
  title: string
  summary: string
  languages: string[]
}

export interface IExperience {
  id: number
  startDate: string
  endDate: string
  title: string
  type: "Full-time" | "Part-time" | "Internship"
  company: string
  imagePath: string
  description: string
  technologies: string[]
  dateAsString?: string
  duration?: string
}

export interface IData {
  metadata: IMetadata
  experience: IExperience[]

  [key: string]: any // Allow indexing by string
}
