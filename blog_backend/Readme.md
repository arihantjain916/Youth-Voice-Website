
# Blog API

This is the API, for blog websites. 


## API Reference

#### Note: 
1. Before using all routes, login is a must because login routes generate JWT token, which is essential to use all routes. 
2. Add Authorization in the header with Bearer.

#### Get all blog

```http
  GET api/details/blogs/
```


#### Get the blog of the user

```http
  GET /api/details/user/${id}/blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to fetch |

#### Get the specific blog

```http
  GET /api/details/${slug}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`    | `string` | **Required**. slug                |

#### create blog 

```http
  POST /api/blog/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | **Required**. title               |
| `content` | `string` | **Required**. content             |

#### update blog 

```http
  PATCH /api/blog/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id to update the blog|


#### delete blog 

```http
  DELETE /api/blog/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id to delete the blog|

#### register new user

```http
  POST /api/user/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. username            |
| `email`   | `string` | **Required**. email               |
| `password`| `string` | **Required**. password            |

#### login user

```http
  POST /api/login/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. username            |
| `password`| `string` | **Required**. password            |

#### Post Comment

```http
  POST /api/comment/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `blog`    | `string` | **Required**. blog id             |
| `comment` | `string` | **Required**. comment             |

#### View Verified Comment

```http
  GET /api/comment/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `blog`    | `string` | **Required**. blog id             |

#### Login with Google

```http
  POST /auth/google/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`auth_token`| `string` | **Required**. auth token received by google oauth|

#### Contact-Us

```http
  POST /contact-us/
```

| Body      | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`name`     | `string` | **Required**. name                 |
|`email`    | `string` | **Required**. email                |
|`message`  | `string` | **Required**.  message             |





## Run Locally

Clone the project

```bash
  git clone https://github.com/arihantjain916/blog_api.git
```

Go to the project directory

```bash
  cd blog_backend
```

Install dependencies

```bash
  pip install requirements.txt
```
Do Migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```
Create SuperUser

```bash
  python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```


## Roadmap

- Add more integrations

- Check for security loop

- Add Comment functionality(DONE)

- Add contact-us functionality(DONE)

- Integrate Google OAuth(DONE)


