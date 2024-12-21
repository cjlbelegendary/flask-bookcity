function conf_del()
{
    var conf=window.confirm("是否删除")
    fetch('/delete', {
    method: 'POST', // 指定请求方法
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        key: 'value'
    })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}