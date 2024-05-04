#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// #define ITER 7000000
#define ITER 500

int main(int argc, char **argv) {

    // Variables necesarias para medir el tiempo de manera correcta
    struct timeval inicio, final;
    double tiempo; // Tiempo final

    int i, j, a, b = 0, m3 = 8, m5 = 32;

    int N;

    if (argc > 1) {
        N = atoi(argv[1]);
    }

    gettimeofday(&inicio, NULL);

    for (j = 0; j < ITER; j++)
        for (i = 0; i < N; i++) {
            a = i * m3;
            b += a / m5;
        }

    gettimeofday(&final, NULL);
    tiempo = (final.tv_sec - inicio.tv_sec + (final.tv_usec - inicio.tv_usec) / 1.e6);
    double tiempoFinal = tiempo / ITER;

    // printf("Tiempo consumido por el codigo medido: %f\n", tiempo);//De esta manera solo medimos el tiempo del bucle N
    printf("%f\n", tiempo); // De esta manera solo medimos el tiempo del bucle N
}
