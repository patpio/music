const subcategory_change = () => {
    const category_id = document.querySelector('#category').value
    const url = `/categories/${category_id}`

    fetch(url).then(response => response.json()).then((response) => {console.log(response)})
    }

const category = document.querySelector('#category')
category.addEventListener('change',() => {
subcategory_change();
})

subcategory_change();