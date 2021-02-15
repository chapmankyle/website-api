#!/usr/bin/env python3

class Data:
	"""Class representing the backend data that needs to be fetched by the API."""

	m_story = []
	m_projects = []
	m_experience = []
	m_education = []


	def __init__(self):
		self.init_story()
		self.init_projects()
		self.init_experience()
		self.init_education()


	def init_story(self):
		"""Setup the sections in 'Personal Story'."""
		self.m_story = [
			{
				"title": "Date of Birth",
				"year": "1998",
				"icon": "mdi-baby-face",
				"color": "#e06c75",
				"content":
					"I was born on <strong>18 December 1998</strong> at Vergelegen Mediclinic in Somerset West, Cape Town, South Africa. I was told that I was born at roughly 09:00 in the morning and that it was a Friday."
			},
			{
				"title": "My First Pet",
				"year": "2002",
				"icon": "mdi-dog",
				"color": "#61afef",
				"content":
					"I got my first pet Labrador Retriever for my 4<sup>th</sup> birthday party and I immediately fell in love with her. <strong>Tazzy</strong> was her name and she was the most amazing pet I ever had."
			},
			{
				"title": "Started Junior School",
				"year": "2004",
				"icon": "mdi-car-child-seat",
				"color": "#98c379",
				"content":
					"I started my education at <strong>SACS Junior School</strong> in Newlands, Cape Town, South Africa. I used to make paper cell phones, because my mom wouldn't let me have a real phone until I was 13, and paper laptops to pretend that I was a <em>hackerman</em> that could take over the world."
			},
			{
				"title": "Started High School",
				"year": "2012",
				"icon": "mdi-bus-school",
				"color": "#e06c75",
				"content":
					"I started in grade 8 at <strong>SACS High School</strong> and completed my schooling education here. I took Biology, Geography and IT as my three subjects of choice from grades 10 to 12. I was told that we would be doing Java as the main programming language in IT and so I decided to get ahead of the class by studying <em>Javascript</em> in my holidays. Little did I know that <em>Java</em> and <em>Javascript</em> are two completely different programming languages."
			},
			{
				"title": "Started Undergraduate Degree",
				"year": "2017",
				"icon": "mdi-school",
				"color": "#61afef",
				"content":
					"I started my undergraduate degree in a <strong>Bachelor of Science in Mathematical Sciences in Computer Science</strong> at the University of Stellenbosch on 17 January 2017. After three years of study, many late nights and many visits to StackOverflow, I finished my undergraduate degree with 3 distinctions in November 2019.<br /><br />I took a wide variety of modules in my 3 years, namely:<ul><li>Probability Theory and Statistics</li><li>Scientific Communication</li><li>Mathematics</li><li>Economics</li><li>Operations Research</li><li>Applied Mathematics</li><li>Computer Science</li></ul>"
			},
			{
				"title": "Started Postgraduate Degree",
				"year": "2020",
				"icon": "mdi-script",
				"color": "#98c379",
				"content":
					"I started my postgraduate degree in a <strong>Bachelor of Science Honours in Mathematical Sciences in Computer Science</strong> at the University of Stellenbosch on 3 February 2020. After a full year of non-stop work and an ongoing pandemic, I finished my postgraduate degree in November 2020 and aim to start working in January 2021. <br /><br />The modules that I took in the first semester, from February to July, were:<ul><li>Computational Intelligence</li><li>Advanced Algorithms</li><li>Space Science</li></ul><br />The modules that I took in the second semester, from July to November, were:<ul><li>Digital Image Processing</li><li>Functional Programming</li><li>Machine Learning</li></ul>"
			}
		]


	def init_projects(self):
		"""Setup the projects data set."""
		self.m_projects = [
			{
				"title": "Work In Progress: Siege Stats Discord Bot",
				"github": "https://github.com/chapmankyle/siege-stats-bot",
				"languages": "JavaScript",
				"image":
					"https://user-images.githubusercontent.com/43512442/107221283-17736880-6a1c-11eb-85ce-b3ddc9d20088.PNG",
				"description":
					"A Discord bot that displays information about a player of Tom Clancy's Rainbow Six Siege.<br/><br/>I always wanted to try make a Discord bot and so I decided to make a statistics tracker bot for a game that I enjoy playing. The bot is still in very early stages of development, so there are many features in the works. It has been a fun learning experience that involved learning how Discord handles bot interaction and finding out which endpoints Ubisoft exposes in order to retrieve relevant information."
			},
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
				"endYear": "2020",
				"title": "Bachelor of Science Honours degree in Computer Science (BScHons)",
				"place": "University of Stellenbosch",
				"description":
					"I completed my Bachelor of Science degree in Mathematical Sciences in Computer Science, with an honours in Computer Science, in November 2020."
			},
			{
				"color": "#61afef",
				"startYear": "2017",
				"endYear": "2019",
				"title": "Bachelor of Science degree in Computer Science (BSc)",
				"place": "University of Stellenbosch",
				"description":
					"I completed my Bachelor of Science degree in Mathematical Sciences in Computer Science in November 2019."
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
