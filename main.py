#Contributors: Austin Truong and Austin Tran

import fileSearch as fS
import webApp as wA
import time

if __name__ == "__main__":
    start_time = time.time()
    print('-'*8,"LOCAL FILE SEARCH ENGINE", '-'*8)

    wA.app.run(debug=True)

    print("\nProcess finished --- %s seconds ---" % (time.time() - start_time))
