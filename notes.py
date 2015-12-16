concepts = [
  {"lesson_title": "Basics of the Web and HTML",
  "lessons": [
    {"title": "What is the World Wide Web?", 
    "notes": ("The World Wide Web is a collection of "
              "HTML documents, such as plain text, images, links, "
              "and videos. Essentially, the Web is a loop consisting "
              "of four main pieces. You (or me) uses a browser to "
              "display the different HTML docucuments on the internet. "
              "The internet is able to do this by communicating with "
              "servers, computers that host all the HTML documents, "
              "by using HTTP. In total, the World Wide Web consists "
              "of 30 billion pages.")
    },
    {"title": "Basics of HTML",
    "notes": ("HTML HyperText Markup Language is the "
              "basis of much of the internet. It contains text "
              "content with markup that results in what you end "
              "up seeing on a web page. Tags are a crucial part of "
              "HTML, surrounding text contents to form whole elements. "
              "However, there are some tags that don't require closing "
              "tags, called void tags. An example of a void tag is for "
              "the img tag.")
    },
    {"title": '"Computers are Stupid"',
    "notes": ("While not closing a tag might not crash your "
              "browser, it could have a significant impact on how your "
              "HTML is displayed in the browser. Code is, essentially, "
              "written instructions for the computer. Thus, the "
              "instructions must be specific and accurate, or having "
              "proper syntax.")
    },
    {"title": "Inline and Block",
    "notes": ("HTML elements are displayed either Inline or "
              "Block, depending on the tag used. The difference between "
              "the two is important in explaining why some elements are "
              "displayed differently than others.")
    }
  ]
  },

  {"lesson_title": "Creating a Structured Document",
  "lessons": [
    {"title": "Document Object Module",
    "notes": ("...or the DOM, is the tree-like structure of "
              "the HTML page. It consists of all of the elements on the "
              "HTML page. nested inside and outside of other elements. "
	            "An important aspect of the DOM is the interaction between "
	            "HTML and CSS. HTML is the structure of the web page. CSS "
	            "is the style of the web page.")
    },
    {"title": "Everything is a Box",
    "notes": ("Essentially, everything on the web is a box. "
	           "Even a circle is a box...with some help from CSS. This is "
	           "extremely important in Front-End Web Development thinking. "
	           "When you are thinking about how to go from just a graphic "
	           "of a web page to an actual web page, you have to break it "
	           "down into rectangles first, and then go from there.")
    }
  ]
  },

  {"lesson_title": "Adding CSS Style and HTML Structures",
  "lessons": [
    {"title": "Importance of Cascading",
	 "notes": ("The ancestor-descendant relationship is a key "
            "piece in undestanding CSS.Inheritance is the mechanism "
	          "that applies properties to all of an ancestor's "
	          "descendants. This only applies to properties, such as "
	          "color and font. Box-related properties, such as "
	          "background and border, cannot be inherited.")
    },
    {"title": "Avoiding Repetition",
    "notes": ("To be as efficient as possible, you want to "
	           "avoid repeating the same code for similar elements. "
	           "Repetition makes your code, overall, much longer, which "
	           "can make your web page or program run slow. Also, "
	           "repetition will make it difficult for yourself and others " 
	           "to understand your code,and making small changes end up "
	           "taking more time than they should.")
    },
    {"title": "The Box Model",
    "notes": ("Padding, Border, and Margin are three of the "
	           "most important concepts in CSS. Displaying elements "
	           "correctly on the web page requires a clear understanding "
	           "of the relationship all three have with the element's "
	           "contents and other elements on the page.")
    },
    {"title": "Web Page Compatability",
    "notes": ("Different browsers, window sizes, and "
	           "devices could display your HTML and CSS differently. "
	           "To ensure compatability, consider setting sizes in "
	           "terms of percentages, and using the 'box-sizing' "
	           "attribute in your CSS.")
    }         		
  ]
  },

  {"lesson_title": "Unit 4 Notes",
  "lessons": [
    {"title": "Understanding Server Requests",
    "notes": ("The two most common requests between a client and a "
              "server are GET and POST. GET requests request information "
              "from the server, while POST requests submit information "
              "to the server. With each request, the server with send a "
              "response. The most common response codes are 1) 200: "
              "requests were performed successfully 2) 404: request is "
              "incomplete or not found, and 3) 500: There are errors on "
              "the server-side.")
    },
    {"title": "Importance of Validating Input",
    "notes": ("There are a number of reasons that validating user input "
              "is critical in programming. First, the user could alter "
              "the appearance of the web page by entering html markup - "
              "Secondly, hackers can infiltrate your web page without "
              "validation by looking for loop-holes in your code. Lastly, "
              "you want the information that users enter to be what you "
              "are asking for. If you're asking for an email address, you "
              "don't want the user's street address instead. Input validation "
              "is crucial in programming.")
    },
    {"title": "HTML Templates and Abstraction",
    "notes": ("As always, avoiding repetition in programming is essential "
              "in staying efficient, keeping your code readable and fast. "
              "One way to do this with HTML is called Inheritance. With "
              "Inheritance, you can set a base HTML template that includes "
              "elements that are common amongst your other pages. You can "
              "then pass other HTML templates into your base HTML page, "
              "rendering a different page based on the base HTML and the "
              "passed-in content. Avoiding repetition is also important "
              "because it makes you can code quicker, avoid errors, and, "
              "when you need to fix errors, makes that quicker also.")
    }
  ]
  } 
]