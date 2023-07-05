
# Blog API

This is the API, for blog websites. 


## API Reference

#### Note: 
1. Before use all routes, login is must because login route generate JWT token which is essential to use all routes. 
2. Add Autherization in the header with Bearer.

#### Get all blog

```http
  GET /api/
```


#### Get blog of the user

```http
  GET /api/detials/user/${id}/blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to fetch |

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
|`auth_token`| `string` | **Required**. blog id             |

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

Start the server

```bash
  python manage.py runserver
```


## Tech Stack


**Server:** Django


## Roadmap

- Make the frontend using nextjs

- Add more integrations

- Check for security loop

- Add Comment functionality(DONE)

- Add contact-us functionality(DONE)

- Integrate Google OAuth(DONE)


# Hi, I'm Arihant Jain! 👋


## 🚀 About Me
I'm a full stack developer...


## 🛠 Skills
Django, Node.js, SQL, NoSQL, Reactjs, Nextjs


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arihantjain916)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/arihantjain916)


## Feedback

If you have any feedback, please reach out to us at arihantj916@gmail.com


## Support

For support, email arihantj916@gmail.com 

