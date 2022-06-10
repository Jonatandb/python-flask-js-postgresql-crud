const form = document.querySelector('#userForm')
const list = document.querySelector('#userList')

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

  form.reset()
})
