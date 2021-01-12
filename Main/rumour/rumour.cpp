#include <stdio.h>
#include <iostream>
#include <ctime>
using namespace std;

class Receivers{
	int status;
	char name;
	public:
	void UpdateStatus();
	void ShowStatus();
	void setName(char nm);
	int getStatus();
	Receivers(){
		status = 0;
	}
};

class Sender{
	int k, counter;
	public:
	void Blind(Receivers *obj, int len);
	void Feedback(Receivers *obj, int len);
	void Fixed(Receivers *obj,int len);

	Sender(){
	k=3;
	counter =0;
	}

};
void Sender::Blind(Receivers *obj,int len){

    srand((unsigned) time(0));
     int prob = (rand()%10)+1;
// Only looses interest if probability prob is less than  k
//It does not check how many nodes have received the Gossip so no counter is kept
while(k<=prob){
	//If the probability is out of range it sends the message whether or not the node had received it earlier
	//Select A Random Receiver
	int ran = ((rand()%len)+1)-1;
	cout <<"\n Receiver Node: "<<ran;
	cout<<"\n Status of Receiver: "<<obj[ran].getStatus();
	obj[ran].UpdateStatus();
	prob = (rand()%10)+1;

}
//End Blind
}


void Sender::Feedback(Receivers *obj,int len){

    srand((unsigned) time(0));
     int prob = (rand()%10)+1;
// Only Stops Sending Gossip if probability prob is less than  k

    while(k<=prob){
    //If the probability is out of range it sends the message whether or not the node had received it earlier

     //Select A Random Receiver
    int ran = ((rand()%len)+1)-1;
   //Check receiver Status
    int stat = obj[ran].getStatus();
    counter = counter +1;



    cout <<"\n Receiver Node: "<<ran;
    cout<<"\n Status of Receiver: "<<obj[ran].getStatus();
    obj[ran].UpdateStatus();
    prob = (rand()%10)+1;

    }
//End Feedback
}

void Sender::Fixed(Receivers *obj, int len){
    //Send Message
    srand((unsigned) time(0));
//Loose interest once k nodes have confirmed receiving the message
    while(counter<k){

        int ran = ((rand()%len)+1)-1;
     int stat = obj[ran].getStatus();

     if (stat==1){
        //The Receiver Selected Got The message
        //Increase Counter
         counter = counter + 1;
        cout<<"\n Counter1: "<<counter;
        continue;
     }else{
        //The Receiver Did Not Get The Gossip
        //Pass The Gossip by changing status value
        obj[ran].UpdateStatus();
       // counter = counter + 1;
        //cout<<"\n Counter else: "<<counter;


     }


     //cout <<"Random: "<<ran;
    }



}
void Receivers::UpdateStatus(){
    status = 1;
}
void Receivers::setName(char nm){
    name = nm;
}
void Receivers::ShowStatus(){
     cout<<"Status: "<<status;
}
int Receivers::getStatus(){
     return status;
}

int main(){
    Receivers obj[4];
    Sender P;
    char name;
    //Size of object
     int si = sizeof(obj)/sizeof(*obj);
    for(int i =0; i<=si;i++){
        cout<<"\n Enter Node Name: ";
        cin>>name;
        obj[i].setName(name);
    }


}

