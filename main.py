# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import BubbleSort, CocktailSort, QuickSort, InsertSort



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Example_Items = BubbleSort.BubbleSort()
    Example_Items.FullRandom(10)
    Example_Items.Sort()

    CocktailItem = CocktailSort.CocktailSort()
    CocktailItem.FullRandom(10)
    CocktailItem.Sort()

    QuickItem = QuickSort.QuickSort()
    QuickItem.FullRandom(10)
    QuickItem.Sort()

    InsertItem = InsertSort.InsertSort()
    InsertItem.FullRandom(10)
    InsertItem.Sort()

    print('Отсортированный массив (сортировка вставками)')
    for i in InsertItem.items:
        print(i)

    print()
    print('Отсортированный массив(БЫстрая сортировка)')
    for i in QuickItem.items:
        print(i)


    print('Отсортированный массив')
    for i in Example_Items.items:
        print(i)
    #print(type(Exa
    #
    #mple_Items))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    print('Отсортированный массив')
    for i in CocktailItem.items:
        print(i)