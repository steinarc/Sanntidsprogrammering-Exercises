#include <pthread.h>
#include <stdio.h>

int i = 0;
pthread_mutex_t mutex;

// Note the return type: void*
void* someThreadFunction1(){
     int x;
     for (x = 0; x < 1000000; x++){
	pthread_mutex_lock(&mutex);
		i++;
	pthread_mutex_unlock(&mutex);	
	}
    return NULL;
}

void* someThreadFunction2(){
    int x;
    for (x  = 0; x < 1000001; x++){
	pthread_mutex_lock(&mutex);
		i--;
	pthread_mutex_unlock(&mutex);	
	}
    return NULL;
}


int main(){
    pthread_t someThread1;
    pthread_t someThread2;

    pthread_create(&someThread1, NULL, someThreadFunction1, NULL);
    pthread_create(&someThread2, NULL, someThreadFunction2, NULL);

    // Arguments to a thread would be passed here ---------^
    
    pthread_join(someThread1, NULL);
    pthread_join(someThread2, NULL);

    printf("%i\n", i);
    return 0;
    
}
