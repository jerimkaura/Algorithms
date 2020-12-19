#include<iostream>
using namespace std;
int main (){
    int temp;
    int list[7] = {12, 34, 22, 56, 70, 45,33};
    cout<<"The unsorted list:"<<endl;
    for (int i = 0; i<7; i++){
        cout<<list[i]<<"\t";
    }
    cout<<endl;

    """ bubble sort works by works by repeatedly swapping the adjacent elements if they are in wrong order."""
    for (int i = 0; i<7; i++){
        for (int j = 0 ; j< 7; j++){
            //swap element[i] & element[j] if element[j] > element[i]
            if(list[j] > list[i]){
                temp = list[j];
                list[j] = list[i];
                list[i] = temp;
            }
        }
    }

    //print the sorted list
    cout<<"\n The sorted list:"<<endl;
    for (int i = 0; i<7; i++){
        cout<<list[i]<<"\t";
    }

    return 0;
}
