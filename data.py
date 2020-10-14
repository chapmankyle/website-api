#!/usr/bin/env python3

class Data:
	"""Class representing the backend data that needs to be fetched by the API."""

	m_projects = []
	m_experience = []
	m_education = []


	def __init__(self):
		self.init_projects()
		self.init_experience()
		self.init_education()


	def init_projects(self):
		"""Setup the projects data set."""
		self.m_projects = [
			{
				"title": "Work In Progress: Carbon Engine",
				"github": "https://github.com/chapmankyle/carbon-engine",
				"languages": "C++",
				"description":
					"A modular graphics engine built using C++ and Vulkan.<br/><br/>The purpose of this graphics engine is to simplify the process of working with Vulkan by abstracting away the tedious work needed to setup both on and off-screen rendering. It is also a learning exercise for me to understand how graphics engines work and how to make my very own.<br/><br/>This engine is in a very early alpha stage, but any criticism or ideas are welcome!"
			},
			{
				"title": "Work In Progress: smath",
				"github": "https://github.com/chapmankyle/smath",
				"languages": "C++",
				"description":
					"A header-only C++ math library designed for use in graphics software.<br/><br/><em>smath</em> is written in C++17, is platform independent and has no external dependencies. Currently, this library includes support for vectors, matrices and converting between degrees and radians.<br/>My aim for this library is to be able to use this in any future games that I develop, so that I have complete control over what all the functions do. It also makes it easier to add new features if the need arises.<br/><br/>Developing this library has been really interesting because I have to constantly learn new things (such as quaternions)."
			},
			{
				"title": "Initialization file (.ini) parser",
				"github": "https://github.com/chapmankyle/dotini",
				"languages": "C++",
				"description":
					"A header-only C++ initialization / configuration file (<code>.ini</code>) parser.<br/><br/><em>dotini</em> is written in C++17, built to favour readability over speed, for now, and stores all parsed key-value pairs inside a map for easy access. I wrote this parser to learn about file parsing in C++ and so that I can use it to read in values set in a <code>.ini</code> and use the values inside my <a href=\"https://github.com/chapmankyle/carbon-engine\">personal game engine</a>.<br/><br/>In the future, I aim to improve the speed of file reading and parsing, as well as possibly adding more features. Any feedback is greatly appreciated!"
			},
			{
				"title": "REST API for Personal Website",
				"github": "https://github.com/chapmankyle/website-api",
				"languages": "Python",
				"description":
					"A RESTful API implemented using Flask and Python.<br/><br/>Everything that you see in this page, and the experience page, is obtained from my REST API so that I can update the REST API with new information instead of updating this website."
			},
			{
				"title": "Personal Website",
				"github": "https://github.com/chapmankyle/website",
				"languages": "VueJS, Javascript, Typescript, HTML, CSS",
				"image":
					"https://user-images.githubusercontent.com/43512442/90319271-d0a62980-df36-11ea-9380-33eef30c6830.png",
				"description":
					"My personal portfolio website that was made using VueJS and Typescript.<br/><br/>I wanted to use my knowledge of web development to create a website for myself, in order to showcase what I have to offer. I made an effort to make my website quite personal so that any person who visits will have a deeper understanding of who I am, as opposed to simply what my experience and qualifications are."
			},
			{
				"title": "Dodger Game",
				"github": "https://github.com/chapmankyle/dodger-game",
				"languages": "Java",
				"image":
					"https://user-images.githubusercontent.com/43512442/88462158-88509a00-cea9-11ea-9362-96e59c16dba9.png",
				"description":
					"Dodger Game is a 2D Java game based on dodging traffic for as long as possible, while other cars come towards you in three different lanes.<br />This was a take on the games that I used to play when I was younger."
			},
			{
				"title": "Epi-Use Portal",
				"github": "https://github.com/chapmankyle/euportal",
				"languages": "React, Flask, HTML, CSS",
				"description":
					"Epi-Use website template that allows businesses to create their own shopping website.<br/>A group of us students created a website for the company Epi-Use."
			},
			{
				"title": "Chatter",
				"github": "https://github.com/chapmankyle/chatter",
				"languages": "Java, SceneBuilder",
				"description":
					"A peer-to-peer communication program written in Java.<br/><br/>A server is set up that listens on a specific port number, then any clients that wish to connect will be connected to the server and can start sending messages to everyone on the server (global chat) or specific people (whisper)."
			},
			{
				"title": "Scripts",
				"github": "https://github.com/chapmankyle/scripts",
				"languages": "Bash",
				"description":
					"Installation scripts for various Linux programs that I have needed to install over the years."
			},
			{
				"title": "Dotfiles",
				"github": "https://github.com/chapmankyle/dotfiles",
				"languages": "Bash",
				"description": "Collection of my dotfiles used in my Linux environment."
			}
		]


	def init_experience(self):
		"""Setup the experience data set."""
		self.m_experience = [
			{
				"color": "#e06c75",
				"startDate": "Dec 2019",
				"endDate": "Jan 2020",
				"title": "Web Development Internship",
				"company": "VASTech (Pty) Ltd.",
				"description":
					"I worked on a visualization for geospatial data using OpenLayers, which allowed a user to interact with a map of the world. Various data points could be plotted and played around with in order to visualize specific elements of the data points. I learnt a lot about Vue as a whole, how to integrate OpenLayers with Vue and all the quirks of Javascript/Typescript development.",
				"technologies": ["VueJS", "Javascript", "Typescript", "OpenLayers"]
			},
			{
				"color": "#61afef",
				"startDate": "Jun 2019",
				"endDate": "Jul 2019",
				"title": "Python Internship",
				"company": "VASTech (Pty) Ltd.",
				"description":
					"I worked on a speaker identification program, which took in an audio recording of multiple people speaking and output a separate folder for each speaker in that audio recording. I learnt a lot about the interaction between Python and REST APIs, and how to apply various alterations to audio so that the voices could be separated.",
				"technologies": ["Python", "REST", "cURL"]
			}
		]


	def init_education(self):
		"""Setup the education data set."""
		self.m_education = [
			{
				"color": "#e06c75",
				"startYear": "2020",
				"endYear": "present",
				"title": "Honours Degreee in Computer Science (BScHons)",
				"place": "University of Stellenbosch",
				"description":
					"I am currently in my final year of a BScHons in Mathematical Sciences, Computer Science degree."
			},
			{
				"color": "#61afef",
				"startYear": "2017",
				"endYear": "2019",
				"title": "Bachelor’s Degree in Computer Science (BSc)",
				"place": "University of Stellenbosch",
				"description": "I completed my Bachelor’s Degree in November 2019."
			},
			{
				"color": "#98c379",
				"startYear": "2004",
				"endYear": "2016",
				"title": "Junior and High School",
				"place": "South African College School (SACS)",
				"description":
					"Matriculated with a NSC Bachelor Pass and achieved the following six distinctions:<ul><li>English</li><li>Mathematics</li><li>Information Technology</li><li>Life Sciences</li><li>Geography</li><li>Life Orientation</li></ul>"
			}
		]


	def get_projects(self):
		"""Gets the current projects that I am working on."""
		return self.m_projects


	def get_experience(self):
		"""Gets the job experience that I have."""
		return self.m_experience


	def get_education(self):
		"""Gets the education levels that I have."""
		return self.m_education


	def add_project(self, proj):
		"""Adds a project to the list of projects."""
		self.m_projects.append(proj)


	def add_experience(self, exp):
		"""Adds experience to the list of current experience."""
		self.m_experience.append(exp)


	def add_education(self, ed):
		"""Adds an education to the list of educations."""
		self.m_education.append(ed)
