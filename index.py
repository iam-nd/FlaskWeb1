from flask import Flask, redirect, url_for, flash
from flask import render_template
from flask import request
import urllib.request
from flask import session
import os
from werkzeug.utils import secure_filename
import datetime
from flask_pymongo import PyMongo
import random
from flask_mail import * 


app=Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
"""
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'nibeditadey959@gmail.com'  
app.config['MAIL_PASSWORD'] = 'tutrutunibedita@123'  
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)
"""
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
#mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/project_reg")

mongodb_client = PyMongo(app, uri="mongodb+srv://nibedita123:nibedita123@cluster0.ggyfr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = mongodb_client.db
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


 
@app.route('/')
def indexpage():
    return render_template('index.html')

@app.route('/reg', methods=["GET", "POST"])
def regpage():
    if request.method =='GET':
        return render_template('reg.html')
    else:
        x = datetime.datetime.now() 
        x = ''+str(x)
       # print(x)

        userobj = db.usercollection.find_one(
           {'useremail': request.form['email']}
        )
        if userobj:

            return render_template('reg.html', msg='Already Registered')
        else:
            uname = request.form['fullname']
            db.usercollection.insert_one(
            {'username': uname,
            'useremail': request.form['email'],
            'usermobile': request.form['mobile'],
            'userpass': request.form['password'],
            'regdate':x
             })
            
            
            return render_template('reg.html',msg="REGISTRATION SUCCESSFUL")


@app.route('/log', methods=['GET','POST'])
def log():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = db.usercollection.find_one(
        {'useremail':request.form['email'],
         'userpass':request.form['password']})
        print(user)

        if user:
            session['uemail']= user['useremail']
            session['uname'] = user['username']
            session['usertype']= 'USER'
            return render_template('category.html', uname = user['username'])
        else:
            return render_template('login.html',msg = "INVALID UID OR PASSWORD")


@app.route('/category')
def catpage():
    if request.method == "GET":
        return render_template('category.html', uname = session['uname'])


@app.route('/adminlog', methods=['GET','POST'])  
def adminloginpage(): 
    if request.method == 'GET':
        return render_template('adminlogin.html')
    else:      
        adminuid = request.form['adminuserid']
        adminpass = request.form['adminpassword']

        if(adminuid == 'Nibedita@gmail.com' and adminpass == 'admin'):
            session['aemail']= 'adminuserid'
            session['usertype']= 'admin'
           
            return render_template('dashboard.html')
        else:
            return render_template('adminlogin.html', msg = 'INVALID UID OR PASS')


@app.route('/about')
def aboutpage():
    return render_template('about.html')

   




@app.route('/nature1')
def npage1():
    return render_template('nature1.html')
@app.route('/flower1')
def fpage1():
    return render_template('flower1.html')
@app.route('/festival1')
def festivalpage1():
    return render_template('festival1.html')
@app.route('/green1')
def greenpage1():
    return render_template('green1.html')
@app.route('/music1')
def musicpage1():
    return render_template('music1.html')
@app.route('/auditorium1')
def auditoriumpage1():
    return render_template('auditorium1.html')
@app.route('/food1')
def foodpage1():
    return render_template('food1.html')
@app.route('/cv1.1')
def campus11():
    return render_template('cv1.1.html')
@app.route('/cv2.1')
def campus21():
    return render_template('cv2.1.html')
@app.route('/science1')
def sciencepage1():
    return render_template('science1.html')
@app.route('/game1')
def gamepage1():
    return render_template('game1.html')

@app.route('/workshop1')
def workpage1():
    return render_template('work1.html')
@app.route('/others1')
def otherpage1():
    return render_template('other1.html')







@app.route('/nature')
def npage():
    return render_template('nature.html')
@app.route('/flower')
def fpage():
    return render_template('flower.html')
@app.route('/festival')
def festivalpage():
    return render_template('festival.html')
@app.route('/green')
def greenpage():
    return render_template('green.html')
@app.route('/music')
def musicpage():
    return render_template('music.html')
@app.route('/auditorium')
def auditoriumpage():
    return render_template('auditorium.html')
@app.route('/food')
def foodpage():
    return render_template('food.html')
@app.route('/cv1')
def campus1():
    return render_template('cv1.html')
@app.route('/cv2')
def campus2():
    return render_template('cv2.html')
@app.route('/science')
def sciencepage():
    return render_template('science.html')
@app.route('/game')
def gamepage():
    return render_template('game.html')
@app.route('/todo')
def todopage():
    return render_template('todo.html')
@app.route('/workshop')
def workpage():
    return render_template('work.html')
@app.route('/others')
def otherpage():
    return render_template('other.html')
@app.route('/explore')
def explorepage():
    return render_template('explore.html')

@app.route('/uuploadsearch2', methods=['GET','POST'])
def uuploadsearch2():
    if request.method == 'GET':
        return render_template('randomview2.html')
    else:
        userobj = db.userimageupload.find_one(
        {'category': request.form['category']})
        #print(userobj)

        if userobj:
            #print(userobj['username'])
            return render_template('randomview2.html', userdata = userobj,show_results=1)
        else:

            return render_template('randomview2.html', msg = "INVALID Category")



@app.route('/uuploadsearch', methods=['GET','POST'])
def uuploadsearch():
    if request.method == 'GET':
        return render_template('randomview.html')
    else:
        userobj = db.userimageupload.find_one(
        {'category': request.form['category']})
        #print(userobj)

        if userobj:
            #print(userobj['username'])
            return render_template('randomview.html', userdata = userobj,show_results=1)
        else:

            return render_template('randomview.html', msg = "INVALID Category")

@app.route('/adminhome')  
def adminafterlogin(): 
    return render_template('dashboard.html')

@app.route('/view')  
def viewall(): 
    userobj = db.usercollection.find({})
    print(userobj)
    return render_template('viewall.html', userdata = userobj)

@app.route('/viewcontact')  
def viewallcontact(): 
    userobj = db.contactcollection.find({})
    print(userobj)
    return render_template('contactallview.html', userdata = userobj)

@app.route('/delete5', methods=['POST'])  
def deleteUser5():#userimagedeletebyadmin
    print(request.form['email']) 
    responsefrommongodb = db.contactcollection.find_one_and_delete({'useremail': request.form['email']})
    print(responsefrommongodb)
    return redirect(url_for('viewallcontact'))
    
    


@app.route('/delete1', methods=['POST'])  
def deleteUser1():
    print(request.form['email']) 
    responsefrommongodb = db.usercollection.find_one_and_delete({'useremail': request.form['email']})
    print(responsefrommongodb)
    return redirect(url_for('viewall'))
@app.route('/delete2', methods=['POST'])  
def deleteUser2():#userdelete
    print(request.form['email']) 
    responsefrommongodb = db.usercollection.find_one_and_delete({'useremail': request.form['email']})
    print(responsefrommongodb)
    return redirect(url_for('search'))

 

@app.route('/deleteimage', methods=['POST'])  
def deleteUserimage():#userimagedeletebyuser
    print(request.form['iid']) 
    responsefrommongodb = db.userimageupload.find_one_and_delete({'imageid': request.form['iid']})
    print(responsefrommongodb)
    return redirect(url_for('searchimageadmin'))




@app.route('/delete3', methods=['POST'])  
def deleteUser3():#userimagedeletebyuser
    print(request.form['photoid']) 
    responsefrommongodb = db.userimageupload.find_one_and_delete({'imageid': request.form['photoid']})
    print(responsefrommongodb)
    return redirect(url_for('userimagesearch'))

@app.route('/delete4', methods=['POST'])  
def deleteUser4():#userimagedeletebyadmin
    print(request.form['photoid']) 
    responsefrommongodb = db.userimageupload.find_one_and_delete({'imageid': request.form['photoid']})
    print(responsefrommongodb)
    return redirect(url_for('viewuserimages'))

@app.route('/contact', methods=["POST"])
def contactpage():
    x = datetime.datetime.now() 
    x = ''+str(x)
    db.contactcollection.insert_one(
    {'username': request.form['name'],
    'useremail': request.form['email'],
    'usertext': request.form['message'],
    'contactdate':x
    })
    return render_template('contact.html')

@app.route('/upload', methods=["GET", "POST"])
def uploadpage():
    if request.method =='GET':
        return render_template('upload.html')
    else:
        x = datetime.datetime.now() 
        x = ''+str(x)
        #uname=request.form['name']
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded')
        path='static/uploads/'+filename

        uemail = session['uemail'] #how to retriev value from session //it will work when the session is alredy in login page
        n = str(random.randint(0,9999))
        db.userimageupload.insert_one(
        {
        'imageid':n,
        'username':uemail,
        'uploadimage':path,
        'imagedescription': request.form['text'],
        'category': request.form['category'],
        'useruploaddate':x
        })
        return render_template('upload.html', msg="successfully upload" , filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 



@app.route('/searchimageadmin', methods=['GET','POST'])  #admin, indivisual user image search
def searchimageadmin(): 
    if request.method == 'GET':
        return render_template('searchimageadmin.html')
    else:      
        userobj = db.userimageupload.find_one(
        {'username': request.form['email']})
        print(userobj)
        
        if userobj:
            #print(userobj['username'])
            return render_template('searchimageadmin.html', userdata = userobj,show_results=1)
        else:

            return render_template('searchimageadmin.html', msg = "INVALID EMAIL ID")   

   
@app.route('/search', methods=['GET','POST'])  #admin, indivisual user search
def search(): 
    if request.method == 'GET':
        return render_template('search.html')
    else:      
        userobj = db.usercollection.find_one(
        {'useremail': request.form['email']})
        print(userobj)
        
        if userobj:
            #print(userobj['username'])
            return render_template('search.html', userdata = userobj,show_results=1)
        else:

            return render_template('search.html', msg = "INVALID EMAIL ID")



@app.route('/userimagesearch', methods=['GET','POST'])  
def userimagesearch(): 
   # if request.method == 'GET':
      #  return render_template('userimagesearch.html')
    #else:   
    print(session['uname'])   
    userobj = db.userimageupload.find({'username': session['uemail']})
    print(userobj)          

    if userobj:
        return render_template('userimagesearch.html', userdata = userobj,show_results=1)
    else:
        return render_template('userimagesearch.html', errormsg = "INVALID ID")


@app.route('/userviewprofile')  
def userviewprofile(): 
    uemail = session['uemail']      
    userobj = db.usercollection.find_one({'useremail': uemail})
    print(userobj)
    return render_template('userviewprofile.html', userdata = userobj)

@app.route('/userprofileupdate', methods=["GET", "POST"])  
def updateUserProfile():
    if request.method == 'GET':
        uemail = session['uemail']      
        userobj = db.usercollection.find_one({'useremail': uemail})
        return render_template('updateprofile.html',userdata = userobj)
    else:
        db.usercollection.update_one( {'useremail': session['uemail'] },
        { "$set": { 'usermobile': request.form['mobile'],
                    'userpass': request.form['pass'],
                
                  } 
        })
        return redirect(url_for('userviewprofile'))

@app.route('/beforereset', methods=["GET", "POST"])
def resetpage():
    if request.method == 'GET':
        return render_template('beforereset.html')
    if request.method == 'POST':
      #  uemail = session['uemail']      
      #  userobj = db.usercollection.find_one({'useremail': uemail})
        return render_template('reset.html')#,userdata = userobj)
    else:
        db.usercollection.update_one( {'useremail': session['uemail'] },
        { "$set": { 
                    'userpass': request.form['password'],
                
                  } 
        })
        return redirect(url_for('log'))



@app.route('/viewuserimage')  
def viewuserimages(): 
    userobj = db.userimageupload.find({})
    print(userobj)
    return render_template('viewuserimage.html', userdata = userobj)

@app.route('/userprofile')  
def userprofile(): 
    return render_template('userprofile.html')

@app.route('/logout')  
def logout():  
    if 'usertype' in session:
        utype = session['usertype']
        if utype == 'USER':
            session.pop('usertype',None)
        else: 
            session.pop('usertype',None)
            session.pop('uemail',None)
            session.pop('uname',None)
        return redirect(url_for('indexpage'));    
    else:  
        return '<p>user already logged out</p>' 

@app.route('/logoutadmin')  
def logoutadmin():  
    if 'usertype' in session:
        utype = session['usertype']
        if utype == 'admin':
            session.pop('usertype',None)
        else: 
            session.pop('usertype',None)
            session.pop('aemail',None)
          
        return redirect(url_for('indexpage'));    
    else:  
        return '<p>user already logged out</p>' 


if __name__=='__main__':
    app.run(debug = True)        
