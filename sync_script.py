# import subprocess
# import time

# # Set the paths to the repositories
# repo1_path = '/home/maram/Github/Common'
# repo2_path = '/home/maram/Github/Test/Common'

# # Set the delay in seconds between sync operations
# delay = 60  # 5 minutes

# def sync_repos():
#     # Change directory to repo1 and pull changes
#     subprocess.run(['git', '-C', repo1_path, 'pull'])

#     # Change directory to repo2, add changes, commit, and push
#     subprocess.run(['git', '-C', repo2_path, 'add', '.'])
#     subprocess.run(['git', '-C', repo2_path, 'commit', '-m', 'Sync changes'])
#     subprocess.run(['git', '-C', repo2_path, 'push'])

# while True:
#     sync_repos()
#     time.sleep(delay)
