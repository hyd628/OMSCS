# Frequently Asked Questions

## What providers is zklogin compatible with?

zkLogin is designed to work with the [OpenID](https://openid.net/) distributed identity standard. 

Currently Sui zklogin supports Google, Facebook and Twitch. More OpenID compatible providers will be enabled in the future. 

## Will my zkLogin Address change?

zkLogin address is derived from `sub`, `iss`, `aud` and `user_salt`.

The address will not change if you log in to the same wallet with the same OAuth provider, since `sub`, `iss` and `aud` (see [definitions](../content/how_zklogin_works.md#definitions)) that remain unchanged in the JWT token, even though the JWT token itself may look different every time a user logs in.

However, if you log in with different OAuth providers, your address will change because the `iss` and `aud` are defined distinctly per provider.

In addition, each wallet or application maintain their own `user_salt`, so logging with the same provider for different wallet may also result in different addresses.

See address definition [here](../content/how_zklogin_works.md#zklogin-address-definition).

## Can I convert a traditional private key wallet into a zkLogin one or retrieve the corresponding mneumonic or private key of a zkLogin wallet?

No. The zkLogin wallet address is derived differently compared to a private key address. Currently zkLogin wallet does not offer portability, the user needs to transfer assets from a zkLogin wallet to a traditional wallet or vice versa.

## Does losing my OAuth credential mean loss of access to the wallet and loss of funds?

Yes. A lost or compromised OAuth credential due to either user action or OpenID provider action could compromise the security of the zklogin wallet or deny the user access to the wallet. 

If someone else can log in with OAuth credential, they can obtain valid JWT token and create valid proofs with any ephemeral key. This means a potential loss of funds in the wallet.

If the user no longer has access to their OAuth credential, they will not be able to access the associated zklogin wallet either. 

## Generating a ZK proof is expensive, is this required for every transcation?

No. The proof generation is only required when ephemeral keypair expires. Since the nonce is defined by the ephemeral public key (`eph_pk`) and expiry (`max_epoch`), the ZK proof is valid until what the expiry is committed to in the JWT token. The ZK proof can be cached and the same ephemeral key can be used to sign transcation till it expires.

See nonce definition [here](./how_zklogin_works.md#notation).

## Is zkLogin Wallet custodial? 

zkLogin wallet is non-custodial. 

A custodial wallet is where a third-party takes custody of the private keys on behalf of the users, and has full control of the assets within that wallet. No such third party exists for zkLogin wallets. 

zkLogin wallet relies on multiple secrets to authenticate the users, including the `user salt` and the OAuth token. A third party may have access to one of the secrets, for example, the OpenID provider may be able to forge the OAuth token, or the wallet may be able to provide the `user salt`, but no parties other than the user should be able to provide all secrets to access the wallet content.

## How is zkLogin different from other providers that supports social login?

mention zkAA, openpubkey, privy, account abstraction in general
also Web3Auth, DAuth

## How is zkLogin different from MPC or multi-sig wallets?

Multi-Party Computation (MPC) and multi-sig wallets rely on sharding keys and distributing the sharded keys to multiple parties, and then defining a threshold value for accepting a signature. 

zkLogin does not shard any individual private keys, but relies on multiple secrets in a similar way. The primary advantage of zkLogin is that the user does not need to manage transaction signature thresholds the same way that an MPC or multisig wallet account would need to. 

## Does zkLogin work on mobile? 

Yes. zkLogin works with any wallet that has completed integration with it, including mobile wallets.  

## What RPC providers support the prover and/or sponsored transactions?

## How can I run my own prover service?

## Is account recovery possible if the user or the wallet loses OAuth credential access? 



