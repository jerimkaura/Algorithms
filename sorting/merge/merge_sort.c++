#include <iostream>
using namespace std;

//merge function
void merge(int arr[], int left,int midpoint, int right){
	int i=left, j = midpoint+1, k = left;//starting points of left, right and temporary sub arrays
	int temp[5] ;
	while(i <= midpoint && j<= right){
		if(arr[i] <= arr[j]){
			temp[k] = arr[i];
			i++;
			k++;
		}else{
			temp[k] = arr[j];
			j++;
			k++;
		}
    }

    // copying all elements in left sub-array to temp
   while(i <= midpoint){
        temp[k] = arr[i];
        i++;
        k++;
   }

    // copying all elements in right sub-array to temp
   while(k <= right){
        temp[k] = arr[j];
        j++;
        k++;
   }

   //copy elements of temp back to the original array
   for(int m = left; m<right ; m++){
       arr[m] = temp[m];
   }
}

//merge sort algorithm
//takes three parameters
void merge_sort(int arr[], int left, int right){
    if(left < right){
        int midpoint = (left+right)/2;
        merge_sort(arr, left, midpoint);
        merge_sort(arr, midpoint+1, right);
        merge(arr, left,midpoint, right);
    }
}

int main() {
    int array[5];
    for(int i=0; i < 5; i++ ){
        cout<<"Enter element: ";cin>>array[i];
    }

    //Before sorting
    cout<<"Before sorting"<<endl;
    for(int i = 0; i<5; i++){
        cout<<" "<<array[i];
    }

    merge_sort(array,0,4);
    //after  sorting
    cout<<endl<<"After sorting";
    for(int i = 0; i<5; i++){
        cout<<array[i]<< " ";
    }

    return 0;

}
