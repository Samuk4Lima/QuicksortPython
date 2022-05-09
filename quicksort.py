def main():
    def Particiona(vet, l, h):
        i = (l - 1)
        pivot = vet[h]

        for j in range(l, h):

            if vet[j] <= pivot:
                i = i + 1
                vet[i], vet[j] = vet[j], vet[i]

        vet[i + 1], vet[h] = vet[h], vet[i + 1]
        return (i + 1)

    def quickSort(vet, l, h):
        if len(vet) == 1:
            return vet
        if l < h:
            partIndex = Particiona(vet, l, h)

            quickSort(vet, l, partIndex - 1)
            quickSort(vet, partIndex + 1, h)

    arr = [6, 7, 3, 6, 0, 9, 8, 21, 4, 65, 22]
    tam = len(arr)
    quickSort(arr, 0, tam - 1)
    print("Vetor ordenado:")
    for i in range(tam):
        print(arr[i])




if __name__ == '__main__':
    main()