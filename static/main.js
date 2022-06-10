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
          <button class="btn-delete btn btn-danger btn-sm">Delete</button>
          <button class="btn-edit btn btn-secondary btn-sm">Edit</button>
        </div>
      </header>
      <p>${user.email}</p>
      <p class="text-truncate">${user.password}</p>
    `

    const btnDelete = userElement.querySelector('.btn-delete')
    btnDelete.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'DELETE',
      })
      const data = await response.json()
      users = users.filter(user => user.id !== data.id)
      renderUsers(users)
    })

    list.append(userElement)
  })
}
