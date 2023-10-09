use std::str::FromStr;
use std::error::Error;
use zingoconfig::ZingoConfig;
use zingoconfig::ChainType;
use zingolib::lightclient::LightClient;
use clap::Parser;

#[derive(Parser,Default,Debug)]
#[clap(author = "Author: Pacu", version, about="A tool that lets you derive addresses quickly from a seed phrase powered by zingo lib")]
/// A Very simple Package Hunter
struct Arguments {
    #[clap(forbid_empty_values = true, validator = validate_seed_phrase_arg)]
    /// BIP-39 Mnemonic Phrase we want to derive the addresses from
    seed_phrase: String,
    /// The number of unified addresses we want to derive from account 0 of this seed.
    address_count: usize,
    #[clap(forbid_empty_values = true, validator = validate_receiver_type)]
    /// The receiver types on the addresses. Valid types: "t", "z", "o", "ot", "zo", "tz", "zo"
    receiver_type: String,
    #[clap(long)]
    verbose: bool,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {   
    println!("=====================================================");
    println!("* Hello! Zcasher!                                   *");
    println!("* This is a testing tool. Do not use in production! *");
    println!("=====================================================");
    let args = Arguments::parse();

    
    let config = ZingoConfig::create_unconnected(ChainType::Regtest, None);
    
    let mnemonic = zingolib::wallet::WalletBase::MnemonicPhrase(String::from_str(&args.seed_phrase).unwrap());
    let client = LightClient::create_unconnected(&config, mnemonic, 1).unwrap();
    let receiver_type = args.receiver_type;

    for _ in 0..(args.address_count - 1) {
        let _ = client.do_new_address(&receiver_type).await.unwrap();
    }

    if args.verbose {
        let addresses = client.do_addresses().await;
        print!("{}",addresses.pretty(4));
    } else {        
        for ua in client.wallet.wallet_capability().read().await.addresses() {
            println!("{}", ua.encode(&config.chain));
        }
    }

    Ok(())
}


fn validate_seed_phrase_arg(name: &str) -> Result<(), String> {
    if name.trim().len() != name.len() {
        Err(String::from(
            "cannot be empty",
        ))
    } else {
        Ok(())
    }
}

fn validate_receiver_type(name: &str) -> Result<(), String> {
    let valid_types =  ["z", "o", "ot", "zo", "tz", "zo"];
    if valid_types.contains(&name) {
        Ok(())
    } else {
        Err(String::from(
                format!("'{}' is not an accepted receiver type. use {:?} instead", name, valid_types)           
            )
        )
    }
}