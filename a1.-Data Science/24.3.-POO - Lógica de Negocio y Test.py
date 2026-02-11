#dataclasses.dataclass: Esta librería sirve para convertir clases normales en contenedores de datos automáticos,
#simplificando así la estructura del código.
#dataclasses.field: Se utiliza cuando un atributo adopte un comportamiento especial, como tener un valor incial, 
#contener metadata, ser una lista, diccionario, conjunto, etc.
from dataclasses import dataclass, field
#enum: Librería que permite declarar enumeraciones (enum) en Python, las cuales son un conjunto de nombres 
#simbólicos (miembros) que están vinculados a valores constantes. Su utilidad principal radica en la legibilidad 
#y mantenibilidad del código, además de que de esta manera se pueden separar datos sensibles que necesitan más 
#seguridad como claves, contraseñas, etc. en un archivo por separado. La sintaxis para usar un enum es:
# - Clase donde se declaran los enums dentro de un archivo file_enums.py:
#       class nombreClasePersonalizadaQueHeredaDeEnum(enum.Enum):
#           NOMBRE_CONSTANTE = VALOR
# - Clase donde se importan los enums para utilizarlos:
#       from path.file_enums import nombreClasePersonalizadaQueHeredaDeEnum
#       constanteEnum = nombreClasePersonalizadaQueHeredaDeEnum.NOMBRE_CONSTANTE.value
from enum import Enum
#typing: Esta librería sirve para indicar y documentar los tipos de datos que se esperan en las variables, 
#parámetros y valores de nuestras clases, sin afectar la ejecución del programa. Su principal objetivo es 
#mejorar la claridad, legibilidad y mantenibilidad del código, permitiendo que los tests detecten errores en los 
#tipos de datos recibidos o mandados entre clases, volviendo el código más fácil de entender, refactorizar y 
#escalar, ya que define contratos claros sobre qué tipo de datos se usan y cómo deben interactuar entre sí.
import typing
#datetime: Librería que proporciona métodos para trabajar con fechas y horas en Python.
from datetime import datetime

"""Este evaluador de renta solicita al aplicante los siguientes datos: application_id, first_name, last_name, 
email, phone_number, user_id y credit_score, además de una o más fuentes de ingreso asociadas a su user_id, 
donde se pide title, employer, gross_income, net_income, start_date, end_date y period_type (Monthly o Yearly). 
El credit_score es proporcionado directamente por el aplicante y representa su historial crediticio, normalmente 
obtenido de un buró de crédito o su reporte oficial.
Al arrendador se le solicitan sus condiciones: monthly_rent, minimum_income_to_rent_ratio y minimum_credit_score. 
Con esta información, la lógica de negocio valida primero que el email no esté vacío, que el credit_score esté 
dentro del rango válido (300-850) y que cumpla el mínimo requerido por el arrendador. Después calcula el 
calculated_monthly_income sumando todos los ingresos del aplicante (convirtiendo los anuales a mensuales cuando 
aplica) y el income_to_rent_ratio dividiendo calculated_monthly_income entre monthly_rent, si este ratio es 
menor al requerido, o si alguna validación previa falla, la aplicación se marca como REJECTED y se listan las 
rejection_reasons; si no hay razones de rechazo, la solicitud se considera ACCEPTED y su application_id se 
incluye en acceptable_applications.
{
  "results": [
    {
      "application": {
        "application_id": 123,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@email.com",
        "phone_number": "+52-555-123-4567",
        "user_id": 1,
        "credit_score": 720
      },
      "income_sources": [
        {
          "title": "Senior Software Engineer",
          "employer": "Tech Corp",
          "gross_income": 5000.0,
          "net_income": 4200.0,
          "start_date": "Jan 01, 2022",
          "end_date": null,
          "user_id": 1,
          "period_type": "Monthly"
        }
      ],
      "landlord_requirements": {
        "monthly_rent": 2000.0,
        "minimum_income_to_rent_ratio": 2.0,
        "minimum_credit_score": 650
      },
      "evaluation": {
        "status": "ACCEPTED",
        "credit_score_valid_range": true,
        "meets_minimum_credit_score": true,
        "calculated_monthly_income": 5000.0,
        "income_to_rent_ratio": 2.5,
        "rejection_reasons": []
      }
    },
    {
      "application": {
        "application_id": 456,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@email.com",
        "phone_number": "+52-555-987-6543",
        "user_id": 2,
        "credit_score": 580
      },
      "income_sources": [
        {
          "title": "Marketing Analyst",
          "employer": "Business Inc",
          "gross_income": 1800.0,
          "net_income": 1500.0,
          "start_date": "Feb 15, 2023",
          "end_date": null,
          "user_id": 2,
          "period_type": "Monthly"
        }
      ],
      "landlord_requirements": {
        "monthly_rent": 2000.0,
        "minimum_income_to_rent_ratio": 2.0,
        "minimum_credit_score": 650
      },
      "evaluation": {
        "status": "REJECTED",
        "credit_score_valid_range": true,
        "meets_minimum_credit_score": false,
        "calculated_monthly_income": 1800.0,
        "income_to_rent_ratio": 0.9,
        "rejection_reasons": [
          "MINIMUM_CREDIT_SCORE_NOT_MET",
          "INCOME_RENT_RATIO_NOT_MET"
        ]
      }
    }
  ],
  "summary": {
    "acceptable_applications": [
      123
    ],
    "rejected_applications": [
      {
        "application_id": 456,
        "rejected_reasons": [
          "MINIMUM_CREDIT_SCORE_NOT_MET",
          "INCOME_RENT_RATIO_NOT_MET"
        ]
      }
    ]
  }
}
"""
# ===================== ENUMS =====================
#IncomePeriodType(str, Enum): Lo que devuelve esta clase es un Enum que se comporta como string, esto dado por 
#el parámetro que recibe (str, Enum), lo que implica que no se tendrá que utilizar la siguiente sintaxis de Enum 
#para acceder a su valor: Enum.value, sino que se accede a él como un string normal.
class IncomePeriodType(str, Enum):  #Hace referencia al tipo de ingreso del aplicante, ya sea mensual o anual.
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
#RejectionReason(Enum): Lo que devuelve esta clase son Enums de tipo RejectionReason, no strings, aunque los 
#Enums contengan strings, y para acceder a su valor, se debe usar la sintaxis: Enum.value.
class RejectionReason(Enum):        #Indica la razón por la que fue rechazada la aplicación de renta.
    INCOME_RENT_RATIO_NOT_MET = "Applicant does not meet the required income to rent ratio."
    INVALID_CREDIT_SCORE_RANGE = "Credit score did not fall within expected range [300-850]"
    NULL_OR_EMPTY_EMAIL = "Email was null or empty."
    MINIMUM_CREDIT_SCORE_NOT_MET = "Credit Score did not meet minimum requirement"


# =================== DATA MODELS ===================
#@dataclass: Esto nos permite evitar cierta sintaxis repetitiva para poder colocar código más simple, donde en 
#vez de poner:
#   class Person:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
#Podemos colocar código equivalente más limpio, sin definir el constructor def __init__(self, ..., param_n)
#explícitamente, ni hacer referencia al parámetro self, que se refiere al objeto futuro que se cree a partir de 
#esta clase, de forma similar a como funciona el concepto de this en otros lenguajes de programación:
#   from dataclasses import dataclass
#   @dataclass
#   class Person:
#       name: str
#       age: int
#Application: Indica datos del usuario como el identificador de su aplicación, nombre, apellido, email, 
#teléfono, id del usuario y su score crediticio. 
@dataclass
class Application:
    application_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    user_id: int
    credit_score: int
#IncomeSource: Indica información de las fuentes de ingreso del usuario, como su puesto, empleador, salario 
#bruto, salario neto, fecha de inicio y de finalización (opcionalmente si está desempleado) en su empleo actual, 
#id del usuario y un objeto de la clase IncomePeriodType, que indica si el ingreso mencionado fue mensual 
#(Monthly) o anual (Yearly).
@dataclass 
class IncomeSource:
    title: str
    employer: str
    gross_income: float
    net_income: float
    #datetime: Asigna el tipo de dato datetime, que hace referencia a un timestamp, el cual incluye fecha y hora.
    start_date: datetime
    #typing.Optional: Indica que una variable puede tener un valor del tipo T o ser None y no levantar errores: 
    #   Optional[T]  ≡  T | None.
    end_date: typing.Optional[datetime]
    user_id: int
    #IncomePeriodType: Clase propia que declara dos enums tipo string: "Monthly" y "Yearly".
    period_type: IncomePeriodType
#LandlordRequirements: Clase que define la renta mensual del departamento, la relación mínima que debe haber 
#entre los ingresos mensuales totales del usuario y su alquier y el score crediticio mínimo para aceptar la 
#aplicación, datos dados por parte del arrendador (el dueño o el que renta el departamento).
@dataclass
class LandlordRequirements:
    monthly_rent: float
    minimum_income_to_rent_ratio: float
    minimum_credit_score: int
#RejectedApplication: Clase que define las aplicaciones que fueron rechazadas, este incluye el identificador de 
#la aplicación y una lista que indica las razones por las que fue rechazada la aplicación, el cual es un objeto 
#de la clase RejectionReason, que a su vez declara 4 enums, encargados de definir las razones del rechazo de la 
#aplicación.
@dataclass
class RejectedApplication:
    application_id: str
    #typing.List[T]: Método que declara una lista cuyos elementos serán de un tipo específico T.
    rejected_reasons: typing.List[RejectionReason]

#dataclasses.field(): Método que configura cómo se crea y se comporta un atributo dentro de una @dataclass. 
#Acepta los siguientes parámetros:
#field(
#     - default = Sirve para configurar valores inmutables de tipo int, float, str, bool o None, y se utiliza 
#       cuando todos los objetos de la clase vayan a tener el mismo valor inicial.
#     - default_factory = Configura valores mutables de tipo Lista [], Diccionarios {}, Conjuntos () u Objetos.
#     - init = Este es un valor booleano True o False que indica si el atributo será incluido en el constructor 
#       o no, de esto dependerá que el valor sea calculado internamente o sea proporcionado por el usuario hacia 
#       la clase, como por ejemplo, un ID autmático.
#     - repr = Es un valor booleano True o False que indica si el campo estará escondido al imprimir el objeto 
#       en consola o no, se utiliza en campos sensibles como contraseñas, tokens, etc.
#     - compare = A través de un booleano True o False se indica si este valor podrá ser utilizado o no en
#       comparaciones lógicas de instancias de la clase (<,>,==,!,etc.), por ejemplo con IDs temporales o campos 
#       irrelevantes para igualdad o desigualdad de objetos.
#     - hash = Valor booleano True o False que indica si algún atributo no debe ser hasheable, esto aplica 
#       cuando la clase creará un iterador zip(), que luego podrá ser utilizado como diccionario (JSON).
#     - metadata = Se asigna un valor None o un diccionario de metadata que querramos incluir como framework,
#       documentación, etc. A través del formato: field(metadata={"required": True, "format": "email"}).
#)
#TestInput: Clase que declara dos listas iniciales, una que instancía a la clase Aplication, la cual indica 
#datos del usuario como el id de su aplicación, nombre, apellido, email, teléfono, id del usuario y su score 
#crediticio, otra que instancía la clase IncomeSource, la cual indica información de las fuentes de ingreso del 
#usuario, como su puesto, empleador, salario bruto, salario neto, fecha de inicio y de finalización (si está 
#desempleado) en su empleo actual, id del usuario y un objeto de la clase IncomePeriodType, que indica si el 
#ingreso mencionado fue mensual (Monthly) o anual (Yearly), finalmente, se crea un objeto de la clase 
#LandlordRequirements la cual indica la renta mensual del departamento, la relación mínima que debe haber entre 
#los ingresos del usuario y el alquier y el score crediticio mínimo para aceptar la aplicación.
@dataclass
class TestInput:                          #Representa la lista "results" en el diccionario final.
    #typing.List[T] = field(default_factory=list): Método que declara una lista cuyos elementos serán de un tipo 
    #específico T y que además siempre iniciará vacía por defecto al crear una nueva instancia de la clase, en 
    #lugar de reutilizar la misma lista entre distintos objetos.
    applications: typing.List[Application] = field(default_factory=list)
    income_sources: typing.List[IncomeSource] = field(default_factory=list)
    landlord_requirements: LandlordRequirements
#ApplicationEvaluatorResponse: Clase que declara dos listas, una que indica todos los identificadores de las 
#aplicaciones que fueron aceptadas (del mismo tipo que application_id) y otra lista que crea una instancia de la 
#clase RejectedApplication, la cual indica el id de las aplicaciones que fueron rechazadas a su vez utiliza un 
#objeto de la clase RejectionReason, que define 4 enums para indicar la razón por la que la aplicación fue 
#rechazada.
@dataclass
class ApplicationEvaluatorResponse:       #Representa el diccionario "summary" en el diccionario final.
    #typing.List[T] = field(default_factory=list): Método que declara una lista cuyos elementos serán de un tipo 
    #específico T y que además siempre iniciará vacía por defecto al crearse una nueva instancia de la clase, en 
    #lugar de reutilizar la misma lista entre distintos objetos.
    acceptable_applications: typing.List[int] = field(default_factory=list)
    rejected_applications: typing.List[RejectedApplication] = field(default_factory=list)


#===================== CORE LOGIC =====================
#evaluate_applications(): Función propia que describe la lógica de negocio de las clases declaradas arriba. 
#En primer lugar lo que hace en su parámetro recibir una instancia de la clase TestInput, la cual recibe las 
#siguientes dos listas de las clases Application ("application") e IncomeSource ("income_sources") y los 
#LandlordRequirements ("landlord_requirements"):
# "application": {
#   "application_id": 123,
#   "first_name": "John",
#   "last_name": "Doe",
#   "email": "john.doe@email.com",
#   "phone_number": "+52-555-123-4567",
#   "user_id": 1,
#   "credit_score": 720
# },
# "income_sources": [
#   {
#     "title": "Senior Software Engineer",
#     "employer": "Tech Corp",
#     "gross_income": 5000.0,
#     "net_income": 4200.0,
#     "start_date": "Jan 01, 2022",
#     "end_date": null,
#     "user_id": 1,
#     "period_type": "Monthly"
#   }
# ],
# "landlord_requirements": {
#   "monthly_rent": 2000.0,
#   "minimum_income_to_rent_ratio": 2.0,
#   "minimum_credit_score": 650
# }
#Y devuelve un objeto ApplicationEvaluatorResponse:
# "summary": {
#   "acceptable_applications": [
#     123
#   ],
#   "rejected_applications": [
#     {
#       "application_id": 456,
#       "rejected_reasons": [
#         "MINIMUM_CREDIT_SCORE_NOT_MET",
#         "INCOME_RENT_RATIO_NOT_MET"
#       ]
#     }
#   ]
# }
#En conclusión, la función ejecuta la lógica del negocio, recibiendo un objeto TestInput y devolviendo un objeto
#ApplicationEvaluatorResponse. 
def evaluate_applications(test_input: TestInput) -> ApplicationEvaluatorResponse:
    #Creación de objeto de la clase @dataclass: Normalmente al instanciar una clase, se le deben pasar los 
    #valores de los parámetros indicados en el constructor, esto ocurre igualmente con las clases de tipo 
    #@dataclass, a excepción de las clases que utilicen el método field(), ya que este define valores iniciales 
    #que no deben ser pasados por el usuario, en este caso entonces:
    # - Application, IncomeSource, LandlordRequirements y RejectedApplication si reciben valores en sus 
    #   parámetros al crear objetos de sus clases.
    # - TestInput y ApplicationEvaluatorResponse no reciben valores porque utilizan el método field().
    response = ApplicationEvaluatorResponse()
    #TestInput: Cada objeto de esta clase puede acceder a las diferentes instancias de las clases Application e 
    #IncomeSource y a la única instancia de la clase LandlordRequirements, cada instancia se llama de la 
    #siguiente forma y a continuación se describen sus atributos internos.
    # - TestInput.applications: Sus atributos internos son application_id, first_name, last_name, email, 
    #   phone_number, user_id y credit_score.
    # - TestInput.income_sources: Sus atributos internos son title, employer, gross_income, net_income, 
    #   start_date, end_date y user_id
    # - TestInput.landlord_requirements: Sus atributos internos son monthly_rent, minimum_income_to_rent_ratio y 
    #   minimum_credit_score.
    landlord = test_input.landlord_requirements     #TestInput.landlord_requirements.
    #Bucle for: Recorre todas las instancias de applications que hayan sido declaradas en el objeto TestInput.
    for app in test_input.applications:             #TestInput.applications.
        reasons: typing.List[RejectionReason] = []

        # 1️⃣ Base validations
        if not app.email:
            reasons.append(RejectionReason.NULL_OR_EMPTY_EMAIL)

        if not (300 <= app.credit_score <= 850):
            reasons.append(RejectionReason.INVALID_CREDIT_SCORE_RANGE)

        if app.credit_score < landlord.minimum_credit_score:
            reasons.append(RejectionReason.MINIMUM_CREDIT_SCORE_NOT_MET)

        # 2️⃣ Monthly income calculation
        monthly_income = 0.0
        for income in test_input.income_sources:
            if income.user_id != app.user_id:
                continue

            if income.period_type == IncomePeriodType.YEARLY:
                monthly_income += income.gross_income / 12
            else:
                monthly_income += income.gross_income

        # 3️⃣ Income-to-rent ratio
        if landlord.monthly_rent > 0:
            ratio = monthly_income / landlord.monthly_rent
            if ratio < landlord.minimum_income_to_rent_ratio:
                reasons.append(RejectionReason.INCOME_RENT_RATIO_NOT_MET)

        # 4️⃣ Final decision
        if reasons:
            response.rejected_applications.append(
                RejectedApplication(app.application_id, reasons)
            )
        else:
            response.acceptable_applications.append(app.application_id)

    return response







#EJERCICIO 2: TABLERO DE BATTELSHIP.
# class tablero():
#     coordenada: dict #Coordenada X: A-J; Coordenada Y: 1-10

# class piezas(tablero):
#     coordenada_inicial: tablero,
#     coordenada_final: tablero,
#     coordenadas_atacadas: tablero

# class jugada(piezas):
#     ataque: tablero,
#     pieza_contrincante: piezas

# class jugadas_anteriores(piezas):
#     ataque: list[jugada]

# class piezas_jugador(piezas):
#     piezas: list[piezas]

# class turno:
#     turno: bool

# class win_lose:
#     win: bool
    
# class jugada_actual_jugada_anterior(jugadas_anteriores):
#     jugada_actual: jugada,
#     jugada_anterior: jugadas_anteriores,
#     piezas_contrincante: piezas_jugador,
#     piezas_jugador: piezas_jugador,
#     turno: turno
    
#     def disparo(ataque, pieza_contrincante):
#         if(ataque.coordenada["X"] > "A") #Dentro del rango del tablero.
#             #Fuera de rango.
#             if(jugada_actual != jugada_anterior): #Lógica de juego, con historial.
#                 #Jugada actual diferente a juagada anterior.
#                 switch turno:
#                     case: True
#                         if(piezas_jugador == ataque):
#                             #Se elimina la pieza.
#                             if(coordenadas_atacadas == coordenada_inicial, coordenada_final):
#                                 piezas_jugador.remove()
#                                 if(piezas_contrincante is Null):
#                                     win_lose = False
#                     case: False
#                         if(piezas_contrincante == ataque):
#                             #Se elimina la pieza.
#                             if(coordenadas_atacadas == coordenada_inicial, coordenada_final):
#                                 piezas_jugador.remove()
#                                 if(piezas_contrincante is Null):
#                                     win_lose = False