import threading

import NetworkConfig
import time

threads = []
threadsPrepare = []
def CheckConsensus(message):

    for i,node in enumerate(NetworkConfig.network.nodes):
        node.broadcastMessage("Broadcast",node.ports,i+1)


    for i,node in enumerate(NetworkConfig.network.nodes):
        print("thread turned on in broad", flush=True)
        # Create a new thread object
        stop_event = False  # This event will be used to signal the thread to stop
        thread = threading.Thread(target=node.checkMessagesBroadcast, args=(stop_event,i+1,))
        thread.daemon = True
        threads.append(thread)
        thread.start()
        print("thread started in broad", flush=True)

    for i,node in enumerate(NetworkConfig.network.nodes):
        print("thread turned on", flush=True)
        stop_event = False  # This event will be used to signal the thread to stop
        thread = threading.Thread(target=node.checkMessagesPrepare, args=(stop_event,i+1,))
        thread.daemon = True
        threadsPrepare.append(thread)
        thread.start()



    time.sleep(90)
    print("Pre-prepare Phase:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ToStringBroadcast()
    print("]", flush=True)


    print("Prepare Phase:", flush=True)

    print("nodes : [", flush=True)

    for node in NetworkConfig.network.nodes:
        node.ToStringPrepare()


    print("]", flush=True)


    print("Commit Phase:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ToStringCommit()

    message
    print("]", flush=True)

    print("The Number Of Messages Dropped in bits is: " + str(NetworkConfig.BitsNumberOfMessagesDropped), flush=True)
    print("The Number Of Messages in bits is: "+str(NetworkConfig.TotalBitsNumberOfMessages),flush=True )

    print("The Number Of Messages Dropped is: " + str(NetworkConfig.NumberOfMessagesDropped), flush=True)
    print("The Number Of Messages  is: " + str(NetworkConfig.TotalNumberOfMessages), flush=True)


    print("Storage:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString()

    message
    print("]", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString2()

    message
    print("]", flush=True)

    print("RCVD:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString()

    message
    print("]", flush=True)

    return True

CheckConsensus("test")