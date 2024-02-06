from aiohttp import web

import webserver_helper as helper
import utils

routes = web.RouteTableDef()


async def start_server():
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()


@routes.get('/ping')
async def ping_service(request):
    return web.Response(text="service available")


@routes.post('/show')
async def show_notification(request):
    text = await request.text()
    success, msg = await helper.show_notification(utils.get_data_from_json(text))
    if success:
        return web.Response(text="notification is showed")
    else:
        return web.Response(text=msg, status=500)


@routes.post('/delete')
async def delete_notification(request):
    text = await request.text()
    success, msg = await helper.delete_notification(utils.get_data_from_json(text))
    if success:
        return web.Response(text="notification has been deleted")
    else:
        return web.Response(text=msg, status=500)


@routes.get('/list')
async def get_list_by_user(request):
    return web.Response(body=helper.get_list())

