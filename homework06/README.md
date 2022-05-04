# Meteorite Landings through Flask, Redis and Kubernetes Cluster

## This has the purpose of allowing the user to post and retrieve data from the meteorite landings file that is stored in a Redis database and orchestrated by a Kubernetes cluster.
1. First, log in to the ISP machine.
2. Second, log in to Kubernetes 
~~~
<username>@coe332-k8s.tacc.cloud 
~~~
Link for the Json file to download manually:
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 


To download to your current directory, paste this command on the terminal:
~~~
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
~~~


## ** How to use the app**
To use this app along with the Kubernetes cluster, you must check if Kubernetes is installed .
To check if Kubernetes has been properly installed, type the following into the terminal:
~~~
kubectl version -o yaml
~~~
If downloaded correctly, information will be printed out. 


## ** Deploying to Kubernetes **

Within a Kubernetes cluster, copy and paste all the .yml in this repository into the directory where Kubernetes is open, starting by the deployment files.
For each file, you must create the pod instance by typing the following into the terminal:
~~~
 kubectl apply -f <file-name>.yml
~~~
This should create instances of the Flask application and Redis server within the Kubernetes cluster that will persist.

Now, you can curl routes from the terminal as long as you have the IP Address of the Flask service.
To find the IP Address, type:
~~~
kubectl get service
~~~
This command will show all the services open in the cluster. Find the one that says 'flask-service', and copy the IP Address listed.

Now, you can use the app methods by typing:
~~~
curl <IP Address>:5000/<method>
~~~
