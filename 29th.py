# author:adarsh raj
# date:11th apr,2023
ep1={234:52,456:96,680:75,532:36}
ep2={352:85,530:35,849:95}


# ep1.update(ep2)  #it will add the content of ep2 to ep1
# ep1.clear()  #it will clear all the content of ep1 and on printing we will get a null dict
# ep1.pop(532)  #it will delete the key named as the given parameter
# ep1.popitem()   #it will simply delete the last key
# del ep1    #it will delete the dictionary named ep1 and on printing we will get an error
del ep1[680]  #it will delete the given key




print(ep1)