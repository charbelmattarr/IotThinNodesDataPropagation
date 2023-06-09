import threading

import NetworkConfig
import time

threads = []
threadsPrepare = []
global doneMsgs


def validateMsg(stop_event):
    while not stop_event:
        doneMsgsNbr = 0
        for node in NetworkConfig.network.nodes:
            if node.state[1] == "done":
                doneMsgsNbr += 1

        if doneMsgsNbr > (NetworkConfig.num_nodes * 2) / 3:
            print("msg is validated.....")
            printTheValuesNeeded()
            stop_event = True
    return
def printTheValuesNeeded():

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


    print("]", flush=True)

    print("The Number Of Messages Dropped in bits is: " + str(NetworkConfig.BitsNumberOfMessagesDropped), flush=True)
    print("The Number Of Messages in bits is: "+str(NetworkConfig.TotalBitsNumberOfMessages),flush=True )

    print("The Number Of Messages Dropped is: " + str(NetworkConfig.NumberOfMessagesDropped), flush=True)
    print("The Number Of Messages  is: " + str(NetworkConfig.TotalNumberOfMessages), flush=True)


    print("Storage:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString()


    print("]", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString2()


    print("]", flush=True)

    print("RCVD:", flush=True)

    print("nodes : [", flush=True)
    for node in NetworkConfig.network.nodes:
        node.ListToString()

    print("]", flush=True)


def CheckConsensus(self,message):

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

    for i,node in enumerate(NetworkConfig.network.nodes):
        print("thread turned on", flush=True)
        stop_event = False  # This event will be used to signal the thread to stop
        thread = threading.Thread(target=node.checkMessagesCommit, args=(stop_event,i+1,))
        thread.daemon = True
        threadsPrepare.append(thread)
        thread.start()

    stop_event = False  # This event will be used to signal the thread to stop
    thread = threading.Thread(target=validateMsg, args=(stop_event,))
    thread.daemon = True
    thread.start()

    return True




CheckConsensus("test")