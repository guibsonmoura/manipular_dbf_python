import dbf


def programa():
    
    tabela_pedidos = dbf.Table(
        filename = 'C:/sicaf/empresa1/dados/PEDIDO2.DbF',
        codepage = 'cp1252',
        
    ).open()

    tabela_pedidos.open(dbf.READ_WRITE)

    tabela_vendas = dbf.Table(
        filename= 'C:/sicaf/empresa1/dados/PEDIDO2.DbF',
        codepage = 'cp1252'
    ).open()

    
    filtered_table = tabela_vendas.pql("select * where data >= 01/04/2023")
    print(filtered_table)
    for record in filtered_table:
        print(record)
    



def main():
    programa()

if __name__ == '__main__':
    main()