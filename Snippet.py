# example_test.py implements a setup_network() that connects all nodes
# We just have to connect nodes 1 and 2 so it is useless for us. So we delete that part
# 
# 
# Now inside run_test(),
# The steps to complete the task 
# 1. Generate a block through node 1 using Generate()
# 2. Send this block to node 2 using syn_block()
# 3. Test if block 2 indeed recieved the block

def run_task(self):
    self.nodes[1].generate(1)
    self.sync_blocks()

assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())

# since the block is trasferred from 1 to 2, getblockhash() should give same value for both nodes.
