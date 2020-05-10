#!/usr/bin/env python
# coding: utf-8

# <a><img src="https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width="200" align="center"></a>

# <h1>Analyzing US Economic Data and  Building a Dashboard  </h1>
# <h2>Description</h2>
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some essential economic indicators from some data, you will then display these economic indicators in a Dashboard. You can then share the dashboard via an URL.
# <p>
# <a href="https://en.wikipedia.org/wiki/Gross_domestic_product"> Gross domestic product (GDP)</a> is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this lab, you will examine how changes in GDP impact the unemployment rate. You will take screen shots of every step, you will share the notebook and the URL pointing to the dashboard.</p>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="#Section_1"> Define a Function that Makes a Dashboard </a></li>
#     <li><a href="#Section_2">Question 1: Create a dataframe that contains the GDP data and display it</a> </li>
#     <li><a href="#Section_3">Question 2: Create a dataframe that contains the unemployment data and display it</a></li>
#     <li><a href="#Section_4">Question 3: Display a dataframe where unemployment was greater than 8.5%</a></li>
#     <li><a href="#Section_5">Question 4: Use the function make_dashboard to make a dashboard</a></li>
#         <li><a href="#Section_6"><b>(Optional not marked)</b> Save the dashboard on IBM cloud and display it</a></li>
#     </ul>
# <p>
#     Estimated Time Needed: <strong>180 min</strong></p>
# </div>
# 
# <hr>

# <h2 id="Section_1"> Define Function that Makes a Dashboard  </h2>

# We will import the following libraries.

# In[127]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In this section, we define the function <code>make_dashboard</code>. 
# You don't have to know how the function works, you should only care about the inputs. The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. If you do not know what an html file is don't worry everything you need to know will be provided in the lab. 

# In[128]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# The dictionary  <code>links</code> contain the CSV files with all the data. The value for the key <code>GDP</code> is the file that contains the GDP data. The value for the key <code>unemployment</code> contains the unemployment data.

# In[129]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# <h3 id="Section_2"> Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.

# <b>Hint: <code>links["GDP"]</code> contains the path or name of the file.</b>

# In[130]:


# Type your code here
df = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv')


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.
# 
# 

# In[131]:


# Type your code here
df.head()


# <h3 id="Section_2"> Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. </h3>

# 
# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.

# In[132]:


# Type your code here
dp = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv')


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.

# In[133]:


# Type your code here
dp.head()


# <h3 id="Section_3">Question 3: Display a dataframe where unemployment was greater than 8.5%. Take a screen-shot.</h3>

# In[134]:


# Type your code here
dp_un = dp[dp['unemployment']>8.5]
dp_un


# <h3 id="Section_4">Question 4: Use the function make_dashboard to make a dashboard</h3>

# In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.

# Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.

# In[135]:


# Create your dataframe with column date
x = df['date']


# Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.

# In[136]:


# Create your dataframe with column change-current
gdp_change = df['change-current']
#gdp_change


# Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.

# In[137]:


# Create your dataframe with column unemployment
unemployment = dp['unemployment']


# Give your dashboard a string title, and assign it to the variable <code>title</code>

# In[138]:


# Give your dashboard a string title
title = 'US Economic Data Dashboard'


# Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.

# In[139]:


file_name = "index.html"


# Call the function <code>make_dashboard</code> , to produce a dashboard.  Assign the parameter values accordingly take a the <b>, take a screen shot of the dashboard and submit it</b>.

# In[140]:


# Fill up the parameters in the following function:
make_dashboard(x,gdp_change,unemployment,title,file_name)


# <h3 id="Section_5"> <b>(Optional not marked)</b>Save the dashboard on IBM cloud and display it  </h3>

# From the tutorial <i>PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD</i> copy the JSON object containing the credentials you created. You’ll want to store everything you see in a credentials variable like the one below (obviously, replace the placeholder values with your own). Take special note of your <code>access_key_id</code> and <code>secret_access_key</code>. <b>Do not delete <code># @hidden_cell </code> as this will not allow people to see your credentials when you share your notebook. </b>

# <code>
# credentials = {<br>
#  &nbsp; "apikey": "eEhxnpG1-QuLD3VuNAZK7tu3MVdmfY7vyKnHh2fh2p9Z",<br>
#  &nbsp; "cos_hmac_keys": {<br>
#  &nbsp;  "access_key_id": "08d11b7ab1214264b5b96caf1619d189", <br>
#  &nbsp;   "secret_access_key": "your-secret-access-key-here"<br>
#  &nbsp; },<br>
# </code>
# <code>
#    &nbsp;"endpoints": "your-endpoints",<br>
#  &nbsp; "iam_apikey_description": "your-iam_apikey_description",<br>
#  &nbsp; "iam_apikey_name": "your-iam_apikey_name",<br>
#  &nbsp; "iam_role_crn": "your-iam_apikey_name",<br>
#  &nbsp;  "iam_serviceid_crn": "your-iam_serviceid_crn",<br>
#  &nbsp;"resource_instance_id": "your-resource_instance_id"<br>
# }
# </code>

# In[141]:


# @hidden_cell
#
credentials = {
  "apikey": "D5CLCfmiRhuelIC9TOjyarEopbw6lfDJ1ffC3iTC-bww",
  "cos_hmac_keys": {
    "access_key_id": "4299253d0ac743f2af095d3c82ffc94f",
    "secret_access_key": "0fdf79435bad3fe35fcacc69807a4b86df494cda1771431a"
  },
  "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "iam_apikey_description": "Auto-generated for key 4299253d-0ac7-43f2-af09-5d3c82ffc94f",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/7e582715cba14530ad0d1ebc4f4ceb2a::serviceid:ServiceId-4e180f3f-2257-4b37-a98d-0f5198f0e79e",
  "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/7e582715cba14530ad0d1ebc4f4ceb2a:443c4ef2-12a7-4480-a974-d401fbc62349::"
}


# You will need the endpoint make sure the setting are the same as <i> PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD </i> assign the name of your bucket to the variable  <code>bucket_name </code> 

# In[152]:


endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'


# From the tutorial <i> PROVISIONING AN OBJECT STORAGE INSTANCE ON IBM CLOUD </i> assign the name of your bucket to the variable  <code>bucket_name </code> 

# In[153]:


bucket_name = '12useconomicdata' # Type your bucket name on IBM Cloud


# 
# We can access IBM Cloud Object Storage with Python useing the <code>boto3</code> library, which we’ll import below:

# In[154]:


import boto3


# We can interact with IBM Cloud Object Storage through a <code>boto3</code> resource object.

# In[155]:


resource = boto3.resource(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]['access_key_id'],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url = endpoint,
)


# We are going to use  <code>open</code> to create a file object. To get the path of the file, you are going to concatenate the name of the file stored in the variable <code>file_name</code>. The directory stored in the variable directory using the <code>+</code> operator and assign it to the variable 
# <code>html_path</code>. We will use the function <code>getcwd()</code> to find current the working directory.

# In[156]:


import os

directory = os.getcwd()
html_path = directory + "/" + file_name


# Now you must read the html file, use the function <code>f = open(html_path, mode)</code> to create a file object and assign it to the variable <code>f</code>. The parameter <code>file</code> should be the variable <code>html_path</code>, the mode should be <code>"r"</code> for read. 

# In[157]:


# Type your code here
f = open(html_path, "r")


# To load your dataset into the bucket we will use the method <code>put_object</code>, you must set the parameter name to the name of the bucket, the parameter <code>Key</code> should be the name of the HTML file and the value for the parameter Body  should be set to <code>f.read()</code>.

# In[158]:


# Fill up the parameters in the following function:
resource.Bucket(name= '12useconomicdata').put_object(Key= 'index.html', Body= f.read())


# In the dictionary <code>Params</code> provide the bucket name  as the value for the key <i>'Bucket'</i>. Also for the value of the key <i>'Key'</i> add the name of the <code>html</code> file, both values should be strings.

# In[159]:


# Fill in the value for each key
Params = {'Bucket': "12useconomicdata" ,'Key': "index.html"}


# The following lines of code will generate a URL to share your dashboard. The URL only last seven days, but don't worry you will get full marks if the URL is visible in your notebook.  

# In[160]:


import sys
time = 7*24*60**2
client = boto3.client(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]['access_key_id'],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url=endpoint,

)
url = client.generate_presigned_url('get_object',Params=Params,ExpiresIn=time)
print(url)


# <h2 id="Section_5">  How to submit </h2>

# <p>Once you complete your notebook you will have to share it to be marked. Select the icon on the top right a marked in red in the image below, a dialogue box should open, select the option all&nbsp;content excluding sensitive code cells.</p>
# 
# <p><img height="440" width="700" src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/EdX/ReadMe%20files/share_noteook1.png" alt="share notebook" /></p>
# <p></p>
# 
# <p>You can then share the notebook&nbsp; via a&nbsp; URL by scrolling down as shown in the following image:</p>
# <p style="text-align: center;"> <img height="308" width="350" src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/EdX/ReadMe%20files/link2.png"  alt="share notebook" /> </p>

# <hr>
# <p>Copyright &copy; 2019 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>

# <h2>About the Authors:</h2> 
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# <p>
# Other contributors: <a href="https://www.linkedin.com/in/yi-leng-yao-84451275/">Yi leng Yao</a>, <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a> 
# </p>

# <h2>References :</h2> 

# <ul>
#  <il>
#      1) <a href="https://research.stlouisfed.org/">Economic Research at the St. Louis Fed </a>:<a href="https://fred.stlouisfed.org/series/UNRATE/"> Civilian Unemployment Rate</a>
#    </il>   
#     <p>
#      <il>
#     2) <a href="https://github.com/datasets">Data Packaged Core Datasets
#        </a>
#    </il> 
#     </p>
#     
# </ul>
# </div>
