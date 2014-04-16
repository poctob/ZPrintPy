# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import web

urls = (
        '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello"
        return greeting
    

if __name__ == "__main__":
    app.run()


