def hello():
    createLink = "<a href='" + someLink + "'>Create a question</a>
    return """<html>
                  <head>
                      <title>Hello</title>
                      <body>
                      """ + createLink + """
                      </body>
              </html>""";