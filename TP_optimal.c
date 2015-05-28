/* Code to find optimal solution for Transportation Problem */

/* 
 * Note: The looping fails for some problems. 
 * Need to check which part of the code is going kaput.
 * Appears to run correctly for most problems I worked out, so, commiting anyway.
 */

#include <stdio.h>

#define true 1
#define false 0

/*
 * M, N, cost matrix, supply and demand are to be provided.
 * Only balanced problems are solved by this program
 */

#define M 3
#define N 3

int cost[M][N] = {
    {2, 2, 3},
    {4, 1, 2},
    {1, 3, 1}
};

int sup[M] = { 10, 15, 40 };
int dem[N] = { 20, 15, 30 };

/* 
 * This matrix indicates whether any allocation is made in a cell 
 * Allocation is marked with '.', which includes dummy allocation also
 * Other cells are marked with ' '                                     
 */
int m[M][N];

int alloc[M][N];                // The values of the allocations in each cell

int u[M], v[N];                 // To find the differences

int diff[M][N] = { {0} };       // the table of differences

int sign[2] = { '+', '-' };

int nodecnt = 1;                // To help filling the alternating + and -
int xi, yi;                     // entering B.V
int xxi, yyi;                   // leaving B.V
void nwcr()
{
    int i, j;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            m[i][j] = ' ';
    i = j = 0;
    while (1) {
        alloc[i][j] = dem[j] < sup[i] ? dem[j] : sup[i];
        sup[i] -= alloc[i][j];
        dem[j] -= alloc[i][j];
        m[i][j] = '.';
        if (sup[i] == 0)
            i += 1;
        else
            j += 1;
        if (i == M - 1 && j == N - 1) {
            alloc[i][j] = dem[j] > sup[i] ? dem[j] : sup[i];
            m[i][j] = '.';
            break;
        }
    }
}

void init_uv()
{
    int cnt = 0, i, j;
    for (i = 0; i < M; i++)
        u[i] = -999;
    for (j = 0; j < N; j++)
        v[j] = -999;
    i = 0;
    j = 0;
    u[0] = 0;
    while (cnt != M + N - 1) {
        for (i = 0; i < M; i++)
            for (j = 0; j < N; j++) {
                if (v[j] == -999 && u[i] != -999 && m[i][j] == '.') {
                    v[j] = cost[i][j] - u[i];
                    cnt++;
                }
                if (v[j] != -999 && u[i] == -999 && m[i][j] == '.') {
                    u[i] = cost[i][j] - v[j];
                    cnt++;
                }
            }
    }
}

void fill_diff()
{
    int i, j;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            diff[i][j] = cost[i][j] - u[i] - v[j];

}

int find_min_diff()
{
    int min = 999, i, j;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            if (min > diff[i][j]) {
                min = diff[i][j];
                xi = i;
                yi = j;
            }
    if (min < 0)
        return 1;               // solution is not optimal yet
    return 0;
}

/* 
 * Traverse from the given point in the given direction.
 * When forming the edge, see that it doesnt go back in the direction it came from 
 */

int traverse(int i, int j, int dir)
{
    if (i >= M || j >= N || i < 0 || j < 0)
        return false;
    if (m[i][j] == ' ') {
        switch (dir) {
        case 'n':
            return traverse(i - 1, j, dir);
        case 's':
            return traverse(i + 1, j, dir);
        case 'e':
            return traverse(i, j + 1, dir);
        case 'w':
            return traverse(i, j - 1, dir);
        }
    }
    if (m[i][j] == 'A')
        return true;
    if (m[i][j] == '+' || m[i][j] == '-' || m[i][j] == ' ') {
        return false;
    }
    // marking as a part of path
    if (m[i][j] == '.') {
        m[i][j] = ' ';
        if (traverse(i + 1, j, 's') && dir != 'n') {
            if (dir == 's') {
                m[i][j] = '.';
            } else {
                m[i][j] = sign[nodecnt];
                nodecnt = !nodecnt;
            }
            return true;
        }
        if (traverse(i - 1, j, 'n') && dir != 's') {
            if (dir == 'n') {
                m[i][j] = '.';
            } else {
                m[i][j] = sign[nodecnt];
                nodecnt = !nodecnt;
            }
            return true;
        }
        if (traverse(i, j + 1, 'e') && dir != 'w') {
            if (dir == 'e') {
                m[i][j] = '.';
            } else {
                m[i][j] = sign[nodecnt];
                nodecnt = !nodecnt;
            }
            return true;
        }
        if (traverse(i, j - 1, 'w') && dir != 'e') {
            if (dir == 'w') {
                m[i][j] = '.';
            } else {
                m[i][j] = sign[nodecnt];
                nodecnt = !nodecnt;
            }
            return true;
        }
        m[i][j] = '.';
    }
    return false;
}

void findloop(int xi, int yi)
{
    m[xi][yi] = 'A';
    nodecnt = 1;
    traverse(xi - 1, yi, 'n');
    traverse(xi, yi + 1, 'e');
    traverse(xi, yi - 1, 'w');
    traverse(xi + 1, yi, 's');
}

/* Find the minimum allocation among the donor cells */
int find_theta()
{
    int i, j, min = 999;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            if (m[i][j] == '-' && min > alloc[i][j]) {
                min = alloc[i][j];
                xxi = i;
                yyi = j;
            }
    return min;
}

void print(int mat[M][N], char c)
{
    int i, j;
    if (c == 'c') {
        for (i = 0; i < M; i++) {
            for (j = 0; j < N; j++) {
                printf("%5c", mat[i][j]);
            }
            puts("");
        }
    } else {
        for (i = 0; i < M; i++) {
            for (j = 0; j < N; j++) {
                printf("%5d", mat[i][j]);
            }
            puts("");
        }
    }
}

void total_cost()
{
    int tc = 0, i, j;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            tc += alloc[i][j] * cost[i][j];
    printf("T.C = %d\n", tc);
}

int main()
{
    int i, j, theta;
    nwcr();
    print(m, 'c');
    puts("");
    print(alloc, 'd');
    puts("");
    init_uv();
    fill_diff();
    print(diff, 'd');
    puts("");
    total_cost();
    puts("");

    while (find_min_diff()) {
        m[xi][yi] = 'A';
        findloop(xi, yi);
        print(m, 'c');
        puts("");
        theta = find_theta();
        for (i = 0; i < M; i++)
            for (j = 0; j < N; j++) {
                if (m[i][j] == '-') {
                    m[i][j] = '.';
                    alloc[i][j] -= theta;
                }
                if (m[i][j] == '+' || m[i][j] == 'A') {
                    m[i][j] = '.';
                    alloc[i][j] += theta;
                }
            }
        m[xi][yi] = '.';
        m[xxi][yyi] = ' ';

        init_uv();
        fill_diff();
        print(alloc, 'd');
        puts("");
        print(diff, 'd');
        puts("");
        total_cost();
        puts("");
    }
    return 0;
}
