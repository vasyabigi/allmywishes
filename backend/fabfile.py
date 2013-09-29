from fabric.api import env, run, cd, settings, prefix, task, sudo


# Server
env.stage = 'prod'
env.hosts = ['192.241.232.177', ]
env.user = 'rambo'
# Db
env.db = 'allmywishes'
env.dbuser = 'pedro'
# Paths
env.project_dir = '/home/rambo/projects/allmywishes'
env.frontend_dir = '/home/rambo/projects/allmywishes/frontend'


@task(alias="pull")
def git_pull():
    with cd(env.project_dir):
        run('git pull origin master')


@task(alias="pip")
def pip_install():
    with settings(cd(env.project_dir), prefix('workon allmywishes')):
        run('pip install -r reqs/%s.txt' % env.stage)


@task(alias="run")
def run_command(command):
    with settings(cd(env.project_dir), prefix('workon allmywishes')):
        run('python manage.py %s --settings="allmywishes.settings.%s"' % (command, env.stage))


@task
def syncdb():
    run_command("syncdb")


@task
def migrate():
    run_command("migrate")


@task(alias="static")
def collectstatic():
    run_command("collectstatic --noinput")


@task(alias="bower")
def bower_install():
    with cd(env.frontend_dir):
        run('bower install')


@task(alias="npm")
def npm_install():
    with cd(env.frontend_dir):
        run('npm install')


@task(alias="dist")
def frontend_dist():
    with cd(env.frontend_dir):
        run('grunt build' % env.stage)


@task(alias="restart")
def restart_supervisor():
    with settings(cd(env.project_dir), prefix('workon allmywishes')):
        sudo('supervisorctl restart allmywishes')


@task
def deploy():
    # backend
    git_pull()
    pip_install()
    syncdb()
    migrate()
    collectstatic()
    # frontend
    npm_install()
    bower_install()
    frontend_dist()
    # server
    restart_supervisor()
