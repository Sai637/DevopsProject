'''
1.Basics of Python
2.	Control Flow
3.	Functions and Scope
4.	Data Structures
5.	Classes and Objects (OOP)
6.	Modules and Packages
7.	Error Handling and Exceptions
8.	File Handling
9.	Iterators and Generators
10.	Comprehensions
11.	Decorators and Closures
12.	Regular Expressions
13.	Multithreading and Multiprocessing
14.	Networking
15.	Database Interaction
16.	Data Science and Visualization (Popular Libraries)
17.	Web Development
18.	Testing and Debugging
19.	Version Control with Git
20.	Advanced Topics
21.	Python Tools and Best Practices
'''

#1.	Basics of Python
#slists
my_list = [1,2.5,"sai",True,1+3j,6]
my_list.append(4)
my_list.insert(2,5)
my_list.extend([6,7,8])
my_list.remove(2.5)
item=my_list.pop(2)
print(item)
del my_list[3]
#del my_list
#my_list.clear()		
print(my_list)
#####################
#indexing
print(my_list[2])
print(my_list[1:2])
print(my_list[:2])
print(my_list[::-1])
#my_list.sort()
print(my_list)

new_list=sorted(my_list)
print(new_list)
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.index(6))
print(my_list.count(6))

sai_list = my_list.copy()
print(sai_list)
####################
#modification
sai_list[1] = 13
print(sai_list)
####################
#checking nd len
print(len(sai_list))
print(2 in sai_list)
print(8 in sai_list)
#######################
#list comprehensions
squared_list = [x **2 for x in sai_list]
print(squared_list)
even_numbers=[x for x in sai_list if x%2 == 0]
print(even_numbers)
######################
#nested list
nest_list=[[1,2],[3,4],[5,6]]
print(nest_list[1])
print(nest_list[1][0])
###############################
#stuple
my_tuple=(1,2,3,4)
#indexing
print(my_tuple[3])
print(my_tuple[1:3])
print(my_tuple[:: -1])
print(my_tuple[-1])

#concate
your_tuple=(5,6,7,8)
both_tuple=my_tuple+your_tuple
print(both_tuple)

repeated_tuple= my_tuple *3
print(repeated_tuple)

#checking
print(4 in my_tuple)
print(2 not in my_tuple)

#len
print(len(my_tuple))
print(my_tuple.count(2))
print(my_tuple.index(3))
#unpacking
a,b,c,d= my_tuple
print(a,b,c,d)










#2.	Control Flow Statements
#sif elif else :
lastball = 4
if lastball >= 6:
    print("Won the match")
elif lastball == 5:
    print("Draw match")
else:
    print("Lost the match")
    
#snestedif

branch_name=input()
build_status =input()
if branch_name == "develop":
    if build_status == "success":
        print("deploying to staging env")
    else:
        print("build failed,Not deploying to staging")
elif branch_name == "master":
    if build_status == "success":
        print("deploying to production env")
    else:
        print("build failed,Not deploying to production")
        
else:
    print("deploying to feature branch,no deployment triggered")
######################################################################  
#sternoryoperator 
import os
print("File exists") if os.path.exists("/home/usr/sai.txt") else print("File does not exist")
#Checks if the file exists at the specified path.

import os
for file_path in ["/home/usr/devops.txt","/home/usr/aws.txt","/home/usr/kubenernetes.txt"]: print(f"{file_path} exists" if os.path.exists(file_path) else f"{file_path} does not exists")

import os
print("all files exists") if all(os.path.exists(file) for file in ["/home/usr/pyhton.txt","/home/usr/devops.txt","/home/usr/aws.txt"]) else print("some files missing")

#sternary operator if elif else
server_status = int(input())
status = "up" if server_status ==1 else "down" if server_status ==0 else "unknown"
print(status)

#sfor loop
sai=75
for memory in range(sai):
    if memory >= 70:
        break
    elif memory < 70:
        print("its ok")
        break
        
n=10
for i in range(n):
    if i <= 25:
        print("low marks")
        
    elif i <=50:
        print(" avg marks")
        break
    elif i <= 75:
        print("good")
        
    else:
        print("exellent")
##################################
#sfor
tasks = ["build", "test", "deploy"]

for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}")
##################################
#snestedfor        
environments = ["development","staging","production"]
servers =["web1","web2","web3"]
for server in servers:
    for env in environments:
        print(f"checking health of {server} in {env} environment")
        
####################################################
#swhile_loop
import time

cpu_usage = 76
while cpu_usage < 90: print("High alert!" if cpu_usage > 80 else "normal usage"); time.sleep(3)
#########################################
import time

cpu_usage = int(input())  
while cpu_usage < 90:
    if cpu_usage > 80:
        print("High alert!")
        break
    else:
        print("normal usage")
        time.sleep(3)
    cpu_usage += 2     
        


########################################
#3.	Functions and Scope
#sfunctions
def greet(name):
    message = f"Good Morning, {name}"
    return message

print(greet("sai"))
print(greet("sai gulivindala"))
##########################################
import math
print(dir(math))
help(math)
##########################################
import inspect
import module_name

print(inspect.getmembers(module_name))
##########################################
import requests

def trigger_jenkins_job(job_name, jenkins_url, token):
    url = f"{jenkins_url}/job/{job_name}/build?token={token}"
    response = requests.post(url)
    if response.status_code == 201:
        print("Jenkins job triggered successfully.")  
    else:
        print(f"Failed to trigger job: {response.status_code}")

trigger_jenkins_job("my-job", "http://jenkins.example.com", "my-token")
'''1.jenkins_url: The base URL of the Jenkins server (e.g., http://jenkins.example.com).
2.token: A token used for authentication to trigger the job. 
This is typically generated within Jenkins for security.
3.Jenkins' REST API provides a way to trigger jobs via the /build endpoint
4.requests.post(): Sends a POST request to the URL to trigger the Jenkins job.
requests is a popular Python library for making HTTP requests.'''
###########################################
def create_terraform_tfvars(instance_data):
    
    tfvars_content = ""
    for data in instance_data:
        tfvars_content += f"""
instance_type = "{data['instance_type']}"
ami_id        = "{data['ami_id']}"
"""
    
    
    with open("terraform.tfvars", "w") as file:
        file.write(tfvars_content)


instance_data = [
    {"instance_type": "t2.micro", "ami_id": "ami-123385646"},
    {"instance_type": "t2.small", "ami_id": "ami-3648026249"},
    {"instance_type": "t2.medium", "ami_id": "ami-845232103"}
]


create_terraform_tfvars(instance_data)

'''1.tfvars_content = "":

Initializes an empty string called tfvars_content.
This string will accumulate the Terraform variable definitions for each instance in the instance_data list.
2.for data in instance_data::

Starts a loop that iterates over each item in instance_data.
data represents one dictionary from the list, which contains keys like instance_type and ami_id.

3.Formatted String (f"""):
Creates a multi-line string using an f-string, which allows the insertion of values directly into the string using placeholders ({}).
4.Appending to tfvars_content:
Each iteration appends a new block of text to tfvars_content.
{data['instance_type']}:
5.Replaces {data['instance_type']} with the value of the instance_type key from the data dictionary.
{data['ami_id']}:
Replaces {data['ami_id']} with the value of the ami_id key from the data dictionary

6. with open("terraform.tfvars", "w") as file:
open():
Opens or creates the file terraform.tfvars.
The first argument, "terraform.tfvars", is the name of the file you want to open.
"w" mode:
The second argument "w" stands for write mode. This means:
If the file already exists, it will be overwritten (its previous content will be erased).
If the file doesn't exist, it will be created.
with statement:
Ensures automatic resource management.
The file is automatically closed once the block of code under with is done, even if an error occurs.
 This prevents issues like leaving a file open accidentally, which could lead to resource leaks or file corruption.'''
##############################################
#sarbitary_arguments
def deploy_apps(*apps):
    for app in apps:
        print(f"Deploying application: {app}...")
        
        print(f"Application {app} deployed successfully ")

deploy_apps("web-app", "api-server", "worker")
##########################################
#skeyword_arguments
def deploy_pod(namespace, image,pod_name):
    print(f"Deploying pod '{pod_name}' in namespace '{namespace}' using image '{image}'.")
    
deploy_pod(pod_name="my-app", namespace="dev", image="nginx:latest")
##############################################
#sarbitary_keyword_arguments
def configure_container(**config):
    print(f"Container configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

configure_container(image="nginx:latest", port="8080", env="production", name="web-server")

##########################################
#sfunctionsinsidenestedfor
import requests

def scrape_prometheus_metrics(exporters, environments):
    for exporter in exporters:
        for env in environments:
            
            url = f"http://{exporter}-{env}.example.com:9090/metrics"
            print(f"Scraping metrics from Prometheus exporter: {url}...")
            
            response = requests.get(url)
            
            if response.status_code == 200:
                print(f"Metrics successfully scraped from {url}.")
            else:
                print(f"Failed to scrape metrics from {url}, Status code: {response.status_code}")

scrape_prometheus_metrics(
    ["api-exporter", "web-exporter"], 
    ["staging", "production"]
)
'''Scraping metrics from Prometheus exporter: http://api-exporter-staging.example.com:9090/metrics...
Failed to scrape metrics from http://api-exporter-staging.example.com:9090/metrics, Status code: 404

Scraping metrics from Prometheus exporter: http://api-exporter-production.example.com:9090/metrics...
Metrics successfully scraped from http://api-exporter-production.example.com:9090/metrics.

Scraping metrics from Prometheus exporter: http://web-exporter-staging.example.com:9090/metrics...
Failed to scrape metrics from http://web-exporter-staging.example.com:9090/metrics, Status code: 500

Scraping metrics from Prometheus exporter: http://web-exporter-production.example.com:9090/metrics...
Metrics successfully scraped from http://web-exporter-production.example.com:9090/metrics.'''

###############################################
#sfunction_inside_nestedif_and _nestedfor
def check_pod_health(namespaces, pods_status):
    for namespace in namespaces:
        print(f"\nChecking pods in namespace: {namespace}...")
        for pod, status in pods_status[namespace].items():
            if status.get("running"):  
                if status.get("ready"):  
                    print(f"Pod {pod} is running and ready.")
                else:
                    print(f"Pod {pod} is running but not ready.")
            else:
                print(f"Pod {pod} is not running.")


pods_status = {
    "namespace1": {
        "pod1": {"running": True, "ready": True},
        "pod2": {"running": True, "ready": False},
        "pod3": {"running": False, "ready": False}
    },
    "namespace2": {
        "pod4": {"running": True, "ready": True},
        "pod5": {"running": False, "ready": False}
    }
}


namespaces = ["namespace1", "namespace2"]

check_pod_health(namespaces, pods_status)

'''Checking pods in namespace: namespace1...
Pod pod1 is running and ready.
Pod pod2 is running but not ready.
Pod pod3 is not running.

Checking pods in namespace: namespace2...
Pod pod4 is running and ready.
Pod pod5 is not running.'''

###############################################
#sfunctioninsidewhile
import requests
import time

def send_health_alert(app_name):
    print(f"ALERT: {app_name} is down!")

def monitor_app_health(app_name, health_url, poll_interval=10):
    while True:
        
        response = requests.get(health_url)
        
        if response.status_code == 200:
            print(f"{app_name} is healthy.")
        else:
            send_health_alert(app_name)
            break
        
        time.sleep(poll_interval)


monitor_app_health("MyApp", "http://myapp.example.com/health", poll_interval=5)
'''MyApp is healthy.
MyApp is healthy.
ALERT: MyApp is down!
'''
################################################
#sternaryoperatorfunction
import boto3; boto3.client('s3').upload_file('local_file.txt', 'my-bucket', 's3_file.txt')
########################################################
#slambdafunction
import boto3
list_s3_buckets = lambda: [print(bucket['Name']) for bucket in boto3.client('s3').list_buckets()['Buckets']]
list_s3_buckets()
###########################################################################################################
import boto3
list_iam_users = lambda: [print(user['UserName']) for user in boto3.client('iam').list_users()['Users']]
list_iam_users()



###############################################

#4.	Data Structures
list=["sai","Gulivindala",2,3.5]
print(list)
list.pop(2)
print(list)

#slists
import random
import time

servers = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

for server in servers:
    print(f"Pinging server: {server}...")
    
    success = random.choice([True, False])
    
    if success:
        print(f"Server {server} is reachable.")
    else:
        print(f"Failed to reach server {server}.")
    
    time.sleep(1)

print("Ping operation completed for all servers.")
'''Pinging server: 192.168.1.1...
Server 192.168.1.1 is reachable.
Pinging server: 192.168.1.2...
Failed to reach server 192.168.1.2.
Pinging server: 192.168.1.3...
Server 192.168.1.3 is reachable.
Pinging server: 192.168.1.4...
Failed to reach server 192.168.1.4.
Pinging server: 192.168.1.5...
Server 192.168.1.5 is reachable.
Ping operation completed for all servers.
'''
##############################################
#stuples
tuple1=("sai","Gulivindala",2,3.5,3+5j)
print(tuple1)
#tuple1[]
print(tuple1[1])
####################################################
Database_login = ("gmail","username","password")
Database_login.add("aadhar")
Database_login.remove("password") #if the user add additional data or remove existing data will get error
print(Database_login)
######################################################
# Tuple representing the immutable configuration of a Kubernetes deployment
k8s_deployment_config = ("default", "my-app-deployment", "nginx:latest")

# Accessing elements from the tuple
namespace, deployment_name, container_image = k8s_deployment_config

print(f"Kubernetes Deployment Configuration:")
print(f"Namespace: {namespace}")
print(f"Deployment Name: {deployment_name}")
print(f"Container Image: {container_image}")

# Trying to modify the tuple will raise an error
# k8s_deployment_config[0] = "production"  # Uncommenting this will raise a TypeError
##########################################################
#ssetdatastructure
container1 = {"nginx","busybox","nginx","grafana"}
container2 = {"nginx","helm","prometheus"}
#print(containers_create)#if want to create same name container it will take one container it deletes the duplicate one
containers_soft_both = container1 | container2
print(containers_soft_both)
containers_soft_common = container1 & container2
print(containers_soft_common)
diffrence_containers = container1 - container2
print(diffrence_containers)

############################################################
unique_ips = {"192.168.1.1", "192.168.1.2"}
unique_ips.add("192.168.1.3")
unique_ips.add("192.168.1.1")  # Duplicate, won't be added

print(f"UniqueIPs: {unique_ips}")
################################################################
#sdictionarydatstructure
dict = {"username": "saig","password":"Saigulivindala"}

print(dict)
##############################################################
server_status = {"aws":"running","jenkins": "stopped","kubernetes":"running"}

print(server_status["jenkins"])
server_status["jenkins"] = "running"
print(server_status["jenkins"])
####################################################################
branch_name = input()

git_branches = {
    "main": "a1b2c3d4e5f67890abcdef1234567890",
    "develop": "f0e1d2c3b4a5c6e7d8e9f0b1c2345678",
    "feature-branch": "d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8g9"
}
print(f"The latest commit on {branch_name} is: {git_branches[branch_name]}")

#########################################################################
#squeueds
from queue import Queue
import time
deployment_queue = Queue()

deployment_queue.put("Service-A")
deployment_queue.put("Service-B")
deployment_queue.put("Service-C")

while not deployment_queue.empty():
    service = deployment_queue.get()
    print(f"Deploying: {service}")
    time.sleep(2)  
    deployment_queue.task_done()

print("All deployments complete.")
###################################################################################
#sstackds
from queue import LifoQueue as config_stack
import time

# Create a stack for configuration changes
#config_stack = LifoQueue()

def apply_change(resource, config_change):
    print(f"Applying change to {resource}: {config_change}")
    time.sleep(1)
    config_stack.put((resource, config_change))
    
apply_change("ConfigMap", "added one config data")
apply_change("Deployment", "Update image to v2.0")
apply_change("Service", "Add new endpoint")

def undo_changes():
    while not config_stack.empty():
        resource, config_change = config_stack.get()
        print(f"Undoing change on {resource}: {config_change}")
        time.sleep(1)
    print("All changes undone.")
print("\nError detected! Undoing changes...\n")
undo_changes()
######################################################################
#slinkedlistds
import time
class Pipeline:
    def __init__(self):
        self.stages = []  

    def add_stage(self, name, action):
        self.stages.append((name, action))

    def execute(self):
        for name, action in self.stages:
            print(f"Executing stage: {name}")
            action()
            
        print("Pipeline execution completed.")

# Define actions
def build_action():
    print("Building the application...")
    time.sleep(3)
def test_action():
    print("Running tests...")
    time.sleep(3)
def deploy_action():
    print("Deploying the application...")
    time.sleep(3)
# Create and execute the pipeline
jenkins_pipeline = Pipeline()
jenkins_pipeline.add_stage("Build", build_action)
jenkins_pipeline.add_stage("Test", test_action)
jenkins_pipeline.add_stage("Deploy", deploy_action)

jenkins_pipeline.execute()
#5.	Classes and Objects (OOP)
#s__init__
class person:
    def setvalue(self,name,age):
        self.name = name
        self.age = age
    
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")
p1=person()
name = input()
age = int(input())
p1.setvalue(name,age)
p1.getvalue()

p2=person()
name = input()
age = int(input())
p2.setvalue(name,age)
p2.getvalue()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getvalue(self):
        print(f"the name of the person is {self.name} and age is {self.age}.")

name = input()
age = int(input())
p1=person(name,age)
p1.getvalue()


name = input()
age = int(input())
p2=person(name,age)
p1.getvalue()
#######################################################################
#s__init__
class CICDPipeline:
    def __init__(self, repo_url, branch, environment):
        """
        Initialize the pipeline configuration with repository URL, branch, and deployment environment.
        """
        self.repo_url = repo_url
        self.branch = branch
        self.environment = environment

    def checkout_code(self):
        """
        Simulate code checkout from the repository.
        """
        print(f"Checking out branch '{self.branch}' from repository '{self.repo_url}'.")

    def deploy_code(self):
        """
        Simulate deploying code to the specified environment.
        """
        print(f"Deploying code from branch '{self.branch}' to '{self.environment}' environment.")

    def run_tests(self):
        """
        Simulate running tests in the deployment environment.
        """
        print(f"Running tests on '{self.environment}' environment.")

# Example usage
pipeline = CICDPipeline(
    repo_url="https://github.com/example/myapp.git",
    branch="main",
    environment="production"
)

# Call methods to simulate pipeline tasks
pipeline.checkout_code()
pipeline.deploy_code()
pipeline.run_tests()
'''OUTPUT
Checking out branch 'main' from repository 'https://github.com/example/myapp.git'.
Deploying code from branch 'main' to 'production' environment.
Running tests on 'production' environment.
'''
#####################################################################
'''OOPs Concepts in Python
Inheritance
Polymorphism 
Encapsulation 
Data Abstraction'''
#sInheritance
# Base class for Kubernetes resources
class K8sResource:
    def __init__(self, name, namespace):
        """
        Initialize the Kubernetes resource with name and namespace.
        """
        self.name = name
        self.namespace = namespace

    def get_details(self):
        """
        Simulate retrieving resource details.
        """
        return f"Resource: {self.name}, Namespace: {self.namespace}"

# Derived class for Deployment management
class Deployment(K8sResource):
    def scale(self, replicas):
        """
        Simulate scaling the deployment.
        """
        print(f"Scaling deployment '{self.name}' to {replicas} replicas in namespace '{self.namespace}'.")

# Derived class for Service management
class Service(K8sResource):
    def expose(self, port):
        """
        Simulate exposing the service on a specific port.
        """
        print(f"Exposing service '{self.name}' on port {port} in namespace '{self.namespace}'.")

# Example usage
# Create a Deployment instance
deployment = Deployment(name="my-app", namespace="production")
print(deployment.get_details())
deployment.scale(replicas=3)

# Create a Service instance
service = Service(name="my-app-service", namespace="production")
print(service.get_details())
service.expose(port=8080)

'''OUTPUT:
Resource: my-app, Namespace: production
Scaling deployment 'my-app' to 3 replicas in namespace 'production'.
Resource: my-app-service, Namespace: production
Exposing service 'my-app-service' on port 8080 in namespace 'production'.
'''
############################################################################       
#spolymorphism
class CloudProvider:
    def deploy_instance(self):
        raise NotImplementedError

class AWSProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching EC2 instance in AWS"

class AzureProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching Virtual Machine in Azure"

class GCPProvider(CloudProvider):
    def deploy_instance(self):
        return "Launching Compute Engine instance in GCP"

def provision_cloud_instance(provider: CloudProvider):
    print(provider.deploy_instance())

# Real-time polymorphism
providers = [AWSProvider(), AzureProvider(), GCPProvider()]
for provider in providers:
    provision_cloud_instance(provider)
    

'''OUTPUT
Launching EC2 instance in AWS
Launching Virtual Machine in Azure
Launching Compute Engine instance in GCP
'''
#6.	Modules and Packages
#7.	Error Handling and Exceptions
#8.	File Handling
#9.	Iterators and Generators
#10.Comprehensions
#11. Decorators and Closures
#12. Regular Expressions
#13. Multithreading and Multiprocessing
#14. Networking
#15. Database Interaction
#16. Data Science and Visualization (Popular Libraries)
#17. Web Development
#18. Testing and Debugging
#19. Version Control with Git
#20. Advanced Topics
#21. Python Tools and Best Practices
