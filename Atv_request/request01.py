import requests
import json
import getpass

url = 'http://localhost:3001/api/'


def main():
    option = 0
    while option != -1:
        if option == 0:
            showOptions()
        option = int(getpass.getpass(prompt=''))
        print('-------------------------------')
        if option == 1:
            for item in listProducts():
                print(item[0] + "\t" + item[1] + "\t" + item[2])
            option = 0
        if option == 2:
            id = input('ID: ')
            produto = listProduct(id)
            print('Titulo: ' + produto[0])
            print('Descrição: ' + produto[1])
            print('Url: ' + produto[2] + '\n' )
            option = 0
        if option == 3:
            title = input("Title: ")
            description = input("Description: ")
            link = input("Url: ")
            response = insertProduct(title, description, link)
            print(response)
            option = 0
        if option == 4:
            id = input('ID: ')
            response = deleteProduct(id)
            print(response)
            option = 0
        if option == 5:
            id = input('ID: ')
            title = input("New Title: ")
            description = input("New Description: ")
            link = input("New URL: ")
            response = alterProduct(id, title, description, link)
            print(response)
            option = 0


def showOptions():
    print('-------Products Request--------')
    print('Escolha uma opção:')
    print('1 - Listar Produtos')
    print('2 - Buscar Produto')
    print('3 - Inserir Produto')
    print('4 - Deletar Produto')
    print('5 - Alterar Produto')


def requestAPI(link):
    req = requests.get(link)
    body = json.loads(req.text)
    return body


def listProducts():
    endpoint = 'products/'
    itens = []
    response = requestAPI(url + endpoint)
    for item in response['docs']:
        itens.append([item['_id'], item['title'], item['description']])
    return itens


def listProduct(productID):
    endpoint = 'products/' + productID
    response = requestAPI(url + endpoint)
    product = [
        response['title'], 
        response['description'],
        response['url']
    ]
    return product

def insertProduct(title, description, link):
    endpoint = 'products/'

    body = {'title': title, 'description': description, 'url': link}
    response = requests.post(url + endpoint, json=body)
    return response


def deleteProduct(productID):
    endpoint = 'products/' + productID
    response = requests.delete(url + endpoint)
    return response


def alterProduct(productID, title, description, link):
    endpoint = 'products/' + productID

    body = {'title': title, 'description': description, 'url': link}
    response = requests.put(url + endpoint, json=body)
    return response

if __name__ == "__main__":
    main()