
# Blog API

This is the API, for blog websites. 


## API Reference

#### Get all blog

```http
  GET /api/blog/
```

#### Get blog

```http
  GET /api/blog/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of blog to fetch |

#### Get blog of the user

```http
  GET /api/user/${id}/blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of user to fetch |

#### create blog 

```http
  POST /api/blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | **Required**. title
| `content` | `string` | **Required**. content             |

#### update blog 

```http
  PUT /api/blog/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id to update the blog|


#### delete blog 

```http
  DELETE /api/blog/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id to delete the blog|

#### register new user

```http
  POST /api/user/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required**. name                |
| `email`   | `string` | **Required**. email               |
| `password`| `string` | **Required**. password            |

#### login user

```http
  POST /api/login/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`   | `string` | **Required**. email               |
| `password`| `string` | **Required**. password            |



## Run Locally

Clone the project

```bash
  git clone https://github.com/arihantjain916/blog_api.git
```

Go to the project directory

```bash
  cd Blog_API
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

