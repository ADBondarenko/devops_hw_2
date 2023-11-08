# devops_hw_2
HSE Machine Learning and High Load Systems '25, DevOps, HW2

Автор: Artem Bondarenko, @ArBBBB

ТЗ: 

К нам обратился директор ветеринарной клиники и сказал:
"Клинике необходим микросервис для хранения и обновления информации для собак!"
Директор пообщался с IT-отделом, и они сверстали документацию в формате OpenAPI:

```
openapi: 3.0.2
info:
  title: FastAPI
  version: 0.1.0
paths:
  /:
    get:
      summary: Root
      operationId: root__get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
  /post:
    post:
      summary: Get Post
      operationId: get_post_post_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Timestamp'
  /dog:
    get:
      summary: Get Dogs
      operationId: get_dogs_dog_get
      parameters:
        - required: false
          schema:
            $ref: '#/components/schemas/DogType'
          name: kind
          in: query
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                title: Response Get Dogs Dog Get
                type: array
                items:
                  $ref: '#/components/schemas/Dog'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
    post:
      summary: Create Dog
      operationId: create_dog_dog_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Dog'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dog'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
  /dog/{pk}:
    get:
      summary: Get Dog By Pk
      operationId: get_dog_by_pk_dog__pk__get
      parameters:
        - required: true
          schema:
            title: Pk
            type: integer
          name: pk
          in: path
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dog'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
    patch:
      summary: Update Dog
      operationId: update_dog_dog__pk__patch
      parameters:
        - required: true
          schema:
            title: Pk
            type: integer
          name: pk
          in: path
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Dog'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dog'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Dog:
      title: Dog
      required:
        - name
        - kind
      type: object
      properties:
        name:
          title: Name
          type: string
        pk:
          title: Pk
          type: integer
        kind:
          $ref: '#/components/schemas/DogType'
    DogType:
      title: DogType
      enum:
        - terrier
        - bulldog
        - dalmatian
      type: string
      description: An enumeration.
    HTTPValidationError:
      title: HTTPValidationError
      type: object
      properties:
        detail:
          title: Detail
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
    Timestamp:
      title: Timestamp
      required:
        - id
        - timestamp
      type: object
      properties:
        id:
          title: Id
          type: integer
        timestamp:
          title: Timestamp
          type: integer
    ValidationError:
      title: ValidationError
      required:
        - loc
        - msg
        - type
      type: object
      properties:
        loc:
          title: Location
          type: array
          items:
            anyOf:
              - type: string
              - type: integer
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
```

Необходимо реализовать:

1. Корректно оформлен репозиторий – 1 балл
2. Реализован путь / – 1 балл
3. Реализован путь /post – 1 балла
4. Реализована запись собак – 1 балл
5. Реализовано получение списка собак – 1 балл
6. Реализовано получение собаки по id – 1 балл
7. Реализовано получение собак по типу – 1 балл
8. Реализовано обновление собаки по id – 1 балл
9. Сервис открывается по ссылке – 1 балл
10. Документация совпадает с заданием – 1 балл
