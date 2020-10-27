import rospy
from std_msgs.msg import String


rospy.init_node('node2')

matricula='0'

def recebe_msg(recebido):
    global matricula
    matricula = recebido.data

sub = rospy.Subscriber('/topic1', String, recebe_msg)

def timerCallBack(event):

    soma_matricula = 0
    for digit in matricula:
        soma_matricula +=int(digit)
    msg = String()
    msg.data = str(soma_matricula)
    pub.publish(msg)

pub = rospy.Publisher('/topic2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()