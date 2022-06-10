const form = document.querySelector('#userForm')

let users = []

window.addEventListener('DOMContentLoaded', async () => {
  const response = await fetch('/api/users')
  const data = await response.json()
  users = data
  renderUsers(users)
})

form.addEventListener('submit', async e => {
  e.preventDefault()
  let username = form['username'].value
  let email = form['email'].value
  let password = form['password'].value

  const response = await fetch('/api/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  })

  const data = await response.json()
  users.unshift(data)
  renderUsers(users)
  form.reset()
})

function renderUsers(users) {
  const list = document.querySelector('#userList')
  list.innerHTML = ''
  users.forEach(user => {
    const userElement = document.createElement('li')
    userElement.classList = 'list-group-item list-group-item-dark my-2'
    userElement.innerHTML = `
      <header class="d-flex justify-content-between align-items-center">
        <h3>${user.username}</h3>
        <div>
          <button class="btn btn-danger btn-sm">Delete</button>
          <button class="btn btn-secondary btn-sm">Edit</button>
        </div>
      </header>
      <p>${user.email}</p>
      <p class="text-truncate">${user.password}</p>
    `
    list.append(userElement)
  })
}
