# Code Challenge Python

_Este challenge esta diseñado para resolverse y entregarse como maximo en una semana desde que es enviado al postulante._

## Requerimientos
La Empresa de ESports “Magic Bet” necesita desarrollar un procesador de pagos para sus transacciones de usuarios. Para ello se debe desarrollar una api que gestione las billeteras virtuales de los usuarios de la aplicacion (wallets)
La api debe desarrollarse en python (se puede utilizar por ejemplo Django, Flask o FastApi preferentemente este último) y la misma debe tener los siguientes endpoints.

Tener en cuenta que todas las transacciones que se efectuan contra un user_id deben validar la existencia del usuario en la siguiente base de usuarios:
https://jsonplaceholder.typicode.com/users

> POST /api/credit/{user_id}

- Por medio del payload de la transaccion se enviara el saldo a acreditar en la wallet:
```
{ amount: 100.5} // hasta 2 decimales admitidos
```       

> POST /api/debit/{user_id}

Por medio del payload de la transaccion se enviara el saldo a debitar en la wallet:

    { amount: 100.5} // hasta 2 decimales admitidos

>GET /api/balance/{user_id}

Obtener el saldo actual de la wallet de ese usuario:

>GET /api/balance/users

Obtener el listado de saldos de todos los usuarios de la aplicacion los cuales en el caso de no tener wallet, solo mostrar un mensaje de ‘no transactions’ de modo que la respuesta sea del siguiente estilo:
```
[
    {
        "id": 1,
        "name": "Peter Khan",
        "username": "pkhan",
        "email": "pkhan@mail.es",
        "wallet": {
             "balance" : 30000.00   
        }
    },
    {
        "id": 2,
        "name": "Susan Penn",
        "username": "spenn",
        "email": "rpenn@mail.es",
        "wallet": {
             "balance" : 30000.00   
        }
    },
    {
        "id": 3,
        "name": "Billie Joe",
        "username": "bjoe",
        "email": "bjoe@mail.es",
        "wallet": {
             "message" : "no transaccions"
        }
    },
    ...
]
```

> GET /api/audit/{user_id}

Obtener el listado con el detalle de todas las transacciones realizadas (ver apartado Informacion de transacciones)

>POST /api/withdraw/{user_id}

Por medio del payload de la transaccion se indicara cuanto saldo se desea retirar de la wallet :
    
    { withdraw: 200} // hasta 2 decimales admitidos

En este endpoint no se procedera a descontar el saldo simplemente se validara que la cantidad este disponible y de ser asi se congelara el mismo.

La estrategia para realizar el congelado del saldo puede ser que la entidad encargada en persistir el saldo, tenga un saldo de “congelamiento”, el cual permanezca en cero cuando no se este congelando nada, pero que en el caso de requerir retirar se puede utilizar de la siguiente manera:

- Inicialmente => saldo_wallet = 1000, saldo_congelado = 0
- Se intenta retirar withdraw = 200 => valida si (saldo_wallet - saldo_congelado) > withdraw
- En este caso el servicio procede a congelar el saldo y nos informa que el withdraw es posible => saldo_wallet = 1000, saldo_congelado = 200
- De modo que si se intenta hacer otra transaccion siempre se tendra en cuenta que el saldo disponible son 800, ya que saldo_wallet = 1000 pero saldo_congelado = 200 entonces => saldo_wallet - saldo_congelado = saldo disponoble REAL.

> POST /api/withdraw-confirm/{user_id}

Se procedera a confirmar el retiro del saldo congelado de la wallet para luego realizar la conversion de USD a MATIC, de modo que la api informa el ambos valores, el proceso de confirmacion se realizara de la siguiente manera:

- Con un saldo_wallet = 1000 y saldo_congelado = 200, se procede a descontar los mismos.
- finalmente saldo_wallet = 800 y saldo_congelado = 0 y se procede a realizar la conversion para informar los resultados finales.
- se debe utilizar la api https://docs.cryptowat.ch/cryptowatch-docs/ para obtener el par de conversion MATIC => USD, el mismo se calculara al momento y la finalmente se procedera a revolver la siguiente respuesta:
```
    {
         message: "withdraw succesful",
         withdrawed: {
             USD: 200,
             MATIC: 179.37219
         },
        convertion_rate: 1.115  
     }
```
### Tener en cuenta

Todos los endpoints que accedan a una wallet vinculada al user_id, deben crear la misma con saldo cero, si no hubo transacciones sobre el user_id no se debe crear la wallet.

### Informacion de transacciones

Las transacciones validas e invalidas deben ser registradas en una base de transacciones donde se guarde:

- action => create-wallet / debit / credit / freeze / withdraw
- amount => saldo a aplicar
- description => descripcion de errores

tener en cuenta que ante un intento de debito por encima del saldo o un cualquier otra transaccion invalida se debe informar el detalle del error en la descripcion de la transaccion.

### Se Evaluara
- Robustez.
- Utilizacion de postgresql y migrations para la instalacion de la base de datos.
- Manejo de errores y transacciones invalidas.
- Se valorara uso de unit test.
- Performance, tanto al recuperar datos como en el acceso a los mismos.
- Simplicidad.
- Patrones de diseño (se valora explicar que se uso y porque)
- Clean Coding.
- Entrega
