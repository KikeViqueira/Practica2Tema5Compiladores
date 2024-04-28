#include <stdio.h>
#include <sys/time.h>

#define ITER 5000
#define N 1000

int main(int argc, char **argv) {

    int i, j, a, b = 0;

    // Variables necesarias para medir el tiempo de manera correcta
    struct timeval inicio, final;
    double tiempo, overhead; // Tiempo final

    gettimeofday(&inicio, NULL);

    for (j = 0; j < ITER; j++) {
        for (i = 0; i < N; i++) {
            b += i >> 2;
        }
        a = (N - 1) << 3;
    }

    gettimeofday(&final, NULL);
    tiempo = (final.tv_sec - inicio.tv_sec + (final.tv_usec - inicio.tv_usec) / 1.e6);
    // double tiempoFinal = tiempo / ITER;

    printf("Tiempo consumido por el codigo medido: %f\n", tiempo);
}