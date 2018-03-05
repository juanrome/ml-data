
def ninstances(datafilename):
    datafilename="data/"+datafilename
    datafile=open(datafilename)
    l1=datafile.readline()
    l2=datafile.readline()
    l3=datafile.readline()
    instances=int(l1.split()[1])
    features=int(l2.split()[1])
    labels=int(l3.split()[1])
    print("datafile: ", datafilename, "instances: ", instances, "features: ",
          features, "labels: ", labels, "\n")
    datafile.close()
