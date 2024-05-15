<div align="center">

# Bittex Subnet

</div>

## Overview

Welcome to Bittex, a revolutionary decentralized exchange (DEX) powered by Bittensor, designed to offer the most competitive exchange rates globally. By leveraging the decentralized and dynamic capabilities of Bittensor, Bittex redefines liquidity provision and currency exchange on the blockchain.

From the start of blockchain, decentralized exchanges (DEXs) have been a solid choice for secure, trustless trading. These platforms need a smart system to reward those who supply the funds for trading–known as liquidity providers–because without them, a DEX wouldn't work. Most DEXs, like Uniswap, use complex mathematical formulas to make sure these providers are incentivized, turning these platforms into a good source of passive income for crypto holders.

Despite having a huge community of crypto enthusiasts, Bittensor didn't have its own DEX, which felt like a missed opportunity. Thankfully, Bittensor's ability to create customized incentive mechanisms sets the perfect stage for developing a DEX. Really, all that was missing was a bit of creativity and initiative.

That's where the Bittex subnet comes in. It's a DEX protocol similar to Uniswap but with a twist. In this network, miners are the liquidity providers. These miners are rewarded with TAO from the Bittensor system based on their performance, but instead of using complex math, it lets them compete against each other. The competition among miners to offer the best incentives decides the pricing, making it a real-world, complex calculation that's constantly changing. In this setup, miners are more than just liquidity providers; they're also market makers, actively shaping the prices based on their competition.

At Bittex, we adopt an innovative approach to liquidity provision termed "atomic swaps."<br/>
Unlike traditional DEXs where liquidity providers (LPs) deposit funds into a pool, Bittex requires miners to deposit funds for each swap transaction. This approach significantly reduces the risk of impermanent loss and enhances the efficiency of liquidity provided by our miners.

Bittex is dedicated to revolutionizing the DeFi landscape by striving to become the largest decentralized exchange (DEX) protocol globally. With a focus on offering unparalleled exchange rates and reducing liquidity risks, Bittex harnesses the power of the Bittensor network. This integration not only ensures a secure and efficient trading environment but also positions Bittex at the forefront of innovative market solutions in decentralized finance. Our mission is to reshape how liquidity and currency exchange are managed on the blockchain, setting a new standard for DEX platforms worldwide.

## Architecture

### Introduction to Proof of bid

Proof of bid (PoB) is an underlying protocol that makes sure everything on our platform runs smoothly. At its core lies the smart contract, which guarantees that swap transactions are executed accurately and in accordance with predetermined rules. The contract's integrity is verified and audited by CertiK, underscoring our commitment to a trustworthy platform.

- https://bscscan.com/address/0x4c8cc220d29c19baa2bd8c39ddc27e5d65c7234f/
- https://skynet.certik.com/projects/bittex/

### PoB explained by sequence diagram

<!-- ![Bittex Subnet Sequence Diagram](docs/Bittex%20Subnet%20Sequence%20Diagram.png) -->
<img src="docs/Bittex%20Subnet%20Sequence%20Diagram.png" alt="Bittex Subnet Sequence Diagram" style="width: 100%; max-width: 1000px">

### Scoring mechanism

Miners' scores are calculated based on their activity in each swap, with additional consideration for their ongoing and historical performance:

- Swap-Specific Scoring (85%): For each individual swap, a miner's score is determined by:
  - The bid amount.
  - Inclusion in the top three bids.
  - Being the winning bidder.

- Seven-Day Performance (10%): A miner's activity over the last week influences their score through:
  - The total volume of successful swaps in USD.
  - The number of swaps won.

- Overall Contributions (5%): Recognizing the miner's total tenure, this aspect includes:
  - The total volume of successful swaps in USD.
  - The number of swaps won.

## Links

- **GitHub Repository**: https://github.com/ronx-labs/bittex-subnet/
- **Website**: https://bittex.xyz/
- **App**: https://app.bittex.xyz/
- **X Account**: https://twitter.com/BittexSN/
- **Discord Server**: https://discord.gg/XdAa7BAN8H
- **Smart Contract Deployment**: https://bscscan.com/address/0x4c8cc220d29c19baa2bd8c39ddc27e5d65c7234f/
- **CertiK Security Profile**: https://skynet.certik.com/projects/bittex/
