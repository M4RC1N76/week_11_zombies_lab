from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.biting import Biting
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository


# save 
def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

# select_all
def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for result in results:
        human = human_repository.select(result['human_id'])
        zombie = zombie_repository.select(result['zombie_id'])
        biting = Biting(human, zombie, result['id'])
        bitings.append(biting)

    return bitings

# select

# delete

# delete_all
def delete_all():
    sql = "DELETE  FROM bitings"
    run_sql(sql)

# update